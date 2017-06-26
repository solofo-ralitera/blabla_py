# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)
    roles = models.TextField(null=True)
    last_login = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.__str__()


"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        AppUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.appuser.save()
"""


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
