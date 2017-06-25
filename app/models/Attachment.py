# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Attachment(models.Model):
    author = models.ForeignKey(User)
    type = models.ForeignKey('AttachmentType', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    parameters = models.TextField()
    comments = models.ManyToManyField('Comment')

    def __str__(self):
        return self.name
