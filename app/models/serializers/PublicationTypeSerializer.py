# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from ..PublicationType import PublicationType


class PublicationTypeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=255)
    code = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return PublicationType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance
