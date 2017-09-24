# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .AppUser import AppUser


class Comment(models.Model):
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField('Comment', through='CommentComments')
    # attachments = models.ManyToManyField('Attachment')

    def __str__(self):
        return self.content

    def get_comments(self):
        return self.comments.all()

    def add_comment(self, comment):
        CommentComments(parent=self, comment=comment).save()
        return comment

    def to_array(self):
        comments = dict()
        comments['id'] = self.id
        comments['content'] = self.content
        comments['author'] = self.author.to_array()
        comments['comments'] = [comment.to_array() for comment in self.get_comments() if self.id != comment.id]
        return comments


class CommentComments(models.Model):
    parent = models.ForeignKey('Comment', related_name='parent', on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ''
