# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Publication(models.Model):
    author = models.ForeignKey(User)
    type = models.ForeignKey('PublicationType')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    lang = models.CharField(max_length=6)
    comments = models.ManyToManyField('Comment')
    attachments = models.ManyToManyField('Attachment')

    def __str__(self):
        return self.content
