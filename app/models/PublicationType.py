# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class PublicationType(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.code + ' ' + self.name
