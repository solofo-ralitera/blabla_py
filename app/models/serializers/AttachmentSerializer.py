# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from ..Attachment import Attachment, AttachmentType
from ..AppUser import AppUser


class AttachmentSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    author = serializers.ModelField(model_field=Attachment()._meta.get_field('author'))
    type = serializers.ModelField(model_field=Attachment()._meta.get_field('type'))
    name = serializers.CharField(max_length=255)
    parameters = serializers.CharField()

    class Meta:
        model = Attachment
        fields = ('id', 'author', 'type', 'name', 'parameters')

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
