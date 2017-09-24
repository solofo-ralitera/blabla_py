# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from ..Comment import Comment
from ..AppUser import AppUser


class CommentSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    content = serializers.CharField()
    author = serializers.ModelField(model_field=Comment()._meta.get_field('author'))

    class Meta:
        model = Comment
        fields = ('id', 'content', 'author')

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
