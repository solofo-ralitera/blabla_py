# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .AppUser import AppUser


class Comment(models.Model):
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField('Comment')
    attachments = models.ManyToManyField('Attachment')

    def __str__(self):
        return self.content
