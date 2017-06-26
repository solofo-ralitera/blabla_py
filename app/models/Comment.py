# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from rest_framework import serializers
from .AppUser import AppUser


class Comment(models.Model):
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField('Comment')
    attachments = models.ManyToManyField('Attachment')

    def __str__(self):
        return self.content


class CommentSerializer(serializers.Serializer):
    content = serializers.CharField()
    author = serializers.ModelField(model_field=Comment()._meta.get_field('author'))

    class Meta:
        model = Comment
        fields = ('content', 'author')

    def create(self, validated_data):
        comment = Comment(
            content=validated_data['content'],
        )
        comment.author = AppUser.objects.get(user_id=validated_data['author'])
        comment.save()
        return comment

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.author = AppUser.objects.get(user_id=validated_data.get('author', instance.author))
        instance.save()
        return instance
