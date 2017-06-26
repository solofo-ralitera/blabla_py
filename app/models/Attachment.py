# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from rest_framework import serializers
from .AppUser import AppUser
from .AttachmentType import AttachmentType


class Attachment(models.Model):
    author = models.ForeignKey('AppUser')
    type = models.ForeignKey('AttachmentType', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    parameters = models.TextField()
    comments = models.ManyToManyField('Comment')

    def __str__(self):
        return self.name


class AttachmentSerializer(serializers.Serializer):
    author = serializers.ModelField(model_field=Attachment()._meta.get_field('author'))
    type = serializers.ModelField(model_field=Attachment()._meta.get_field('type'))
    name = serializers.CharField(max_length=255)
    parameters = serializers.CharField()

    class Meta:
        model = Attachment
        fields = ('author', 'type', 'name', 'parameters')

    def create(self, validated_data):
        comment = Attachment(
            name=validated_data['name'],
            parameters=validated_data['parameters'],
        )
        comment.author = AppUser.objects.get(user_id=validated_data['author'])
        comment.type = AttachmentType.objects.get(id=validated_data['type'])
        comment.save()
        return comment

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.parameters = validated_data.get('parameters', instance.parameters)
        instance.author = AppUser.objects.get(user_id=validated_data.get('author', instance.author))
        instance.type = AttachmentType.objects.get(id=validated_data.get('type', instance.type))
        instance.save()
        return instance
