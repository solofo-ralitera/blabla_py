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
    comments = models.ManyToManyField('Comment', through='PublicationComments')
    attachments = models.ManyToManyField('Attachment')

    def __str__(self):
        return self.content

    def get_comments(self):
        return self.comments.all()

    def add_comment(self, comment):
        PublicationComments(publication=self, comment=comment).save()
        return comment


class PublicationComments(models.Model):
    publication = models.ForeignKey('Publication', on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ''
