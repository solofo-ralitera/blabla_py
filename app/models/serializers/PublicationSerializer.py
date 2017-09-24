# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from ..Publication import Publication
from ..PublicationType import PublicationType
from ..AppUser import AppUser


class PublicationSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    author = serializers.ModelField(model_field=Publication()._meta.get_field('author'))
    type = serializers.ModelField(model_field=Publication()._meta.get_field('type'))
    content = serializers.CharField(max_length=255)
    lang = serializers.CharField(max_length=255)

    class Meta:
        model = Publication
        fields = ('id', 'author', 'type', 'content', 'author')

    def create(self, validated_data):
        publication = Publication(
            content=validated_data['content'],
            lang=validated_data['lang'],
        )
        publication.author = AppUser.objects.get(user_id=validated_data['author'])
        publication.type = PublicationType.objects.get(pk=validated_data['type'])
        publication.save()
        return publication

    def update(self, instance, validated_data):
        instance.author = AppUser.objects.get(user_id=validated_data.get('author', instance.author))
        instance.type = PublicationType.objects.get(pk=validated_data.get('type', instance.type))
        instance.content = validated_data.get('content', instance.content)
        instance.lang = validated_data.get('lang', instance.lang)
        instance.save()
        return instance
