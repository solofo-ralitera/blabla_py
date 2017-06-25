# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Follow(models.Model):
    following = models.ForeignKey(User, related_name='following')
    follower = models.ForeignKey(User, related_name='follower')

    def __str__(self):
        return ''

