# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from rest_framework import serializers


class AttachmentType(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=5)

    def __str__(self):
        return self.code + ' ' + self.name

    def to_array(self):
        return AttachmentTypeSerialize(self).data


class AttachmentTypeSerialize(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    code = serializers.CharField(max_length=255)

