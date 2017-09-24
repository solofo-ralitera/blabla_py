# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Follow(models.Model):
    following = models.ForeignKey('AppUser', related_name='following')
    follower = models.ForeignKey('AppUser', related_name='follower')

    def __str__(self):
        return ''

