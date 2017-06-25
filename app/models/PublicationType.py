# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from rest_framework import serializers


class PublicationType(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=5)

    def __str__(self):
        return self.code + ' ' + self.name

    def to_array(self):
        return PublicationTypeSerializer(self).data


class PublicationTypeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    code = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return PublicationType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance
