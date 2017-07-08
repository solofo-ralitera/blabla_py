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
        CommentComments(publication=self, comment=comment).save()
        return comment


class CommentComments(models.Model):
    parent = models.ForeignKey('Comment', related_name='parent', on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ''
