# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from ..AppUser import AppUser


class AppUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    roles = serializers.CharField()
    last_login = serializers.DateTimeField()

    class Meta:
        model = AppUser
        fields = ('username', 'roles', 'last_login',)
        read_only_fields = ('username', 'last_login',)

    def update(self, instance, validated_data):
        instance.roles = validated_data.get('roles', instance.roles)
        instance.save()
        return instance
