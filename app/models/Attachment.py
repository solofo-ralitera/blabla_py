# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .AppUser import AppUser
from .AttachmentType import AttachmentType
from .Comment import Comment


class Attachment(models.Model):
    author = models.ForeignKey('AppUser')
    type = models.ForeignKey('AttachmentType', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    parameters = models.TextField()
    comments = models.ManyToManyField('Comment', through='AttachmentComments')

    def __str__(self):
        return self.name

    def get_comments(self):
        return self.comments.all()

    def add_comment(self, comment):
        AttachmentComments(attachment=self, comment=comment).save()
        return comment


class AttachmentComments(models.Model):
    attachment = models.ForeignKey('Attachment', on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ''

