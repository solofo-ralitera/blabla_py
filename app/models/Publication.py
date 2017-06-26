# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from rest_framework import serializers
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


class PublicationSerializer(serializers.Serializer):
    author = serializers.ModelField(model_field=Publication()._meta.get_field('author'))
    type = serializers.ModelField(model_field=Publication()._meta.get_field('type'))
    content = serializers.CharField(max_length=255)
    lang = serializers.CharField(max_length=255)

    class Meta:
        model = Publication
        fields = ('author', 'type', 'content', 'author')

    def create(self, validated_data):
        publication = Publication(
            content=validated_data['content'],
            lang=validated_data['lang'],
        )
        publication.author = AppUser.objects.get(user_id=validated_data['author'])
        publication.type = PublicationType.objects.get(id=validated_data['type'])
        publication.save()
        return publication

    def update(self, instance, validated_data):
        instance.author = AppUser.objects.get(user_id=validated_data.get('author', instance.author))
        instance.type = PublicationType.objects.get(id=validated_data.get('type', instance.type))
        instance.content = validated_data.get('content', instance.content)
        instance.lang = validated_data.get('lang', instance.lang)
        instance.save()
        return instance
