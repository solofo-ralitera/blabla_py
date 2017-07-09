# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from ..AppUser import AppUser


class AppUserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(source='user.username')
    roles = serializers.CharField()
    last_login = serializers.DateTimeField()

    class Meta:
        model = AppUser
        fields = ('id', 'username', 'roles', 'last_login',)
        read_only_fields = ('id', 'username', 'last_login',)

    def update(self, instance, validated_data):
        instance.roles = validated_data.get('roles', instance.roles)
        instance.save()
        return instance


class AppUserToArray:
    data = []

    def __init__(self, user_list=None, many=True, data=None):
        if user_list:
            if many:
                self.data = []
                for user in user_list:
                    self.data.append(user.to_array())
            else:
                self.data = user_list.to_array()
