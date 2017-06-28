# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .AppUser import AppUser
from .PublicationType import PublicationType


class Publication(models.Model):
    author = models.ForeignKey('AppUser', on_delete=models.CASCADE)
    type = models.ForeignKey('PublicationType')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    lang = models.CharField(max_length=6)
    comments = models.ManyToManyField('Comment')
    attachments = models.ManyToManyField('Attachment')

    def __str__(self):
        return self.content
