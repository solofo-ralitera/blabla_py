# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from rest_framework import serializers
from .AppUser import AppUser
from .AttachmentType import AttachmentType
from .Comment import Comment


class Attachment(models.Model):
    author = models.ForeignKey('AppUser')
    type = models.ForeignKey('AttachmentType', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    parameters = models.TextField()
    comments = models.ManyToManyField('Comment', through='AttachmentComments')

    def __str__(self):
        return self.name

    def get_comments(self):
        return AttachmentComments.objects.filter(attachment=self)

    def add_comment(self, comment):
        AttachmentComments(attachment=self, comment=comment).save()
        return comment


class AttachmentComments(models.Model):
    attachment = models.ForeignKey('Attachment', on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ''


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


class AttachmentCommentSerializer(serializers.Serializer):
    attachment = serializers.ModelField(model_field=AttachmentComments()._meta.get_field('attachment'))
    comment = serializers.ModelField(model_field=AttachmentComments()._meta.get_field('comment'))

    def create(self, validated_data):
        at = AttachmentComments()
        at.attachment = Attachment.objects.get(id=validated_data['attachment'])
        at.comment = Comment.objects.get(id=validated_data['comment'])
        at.save()
        return at

    def update(self, instance, validated_data):
        instance.attachment = Attachment.objects.get(id=validated_data.get('attachment', instance.attachment))
        instance.comment = Comment.objects.get(id=validated_data.get('comment', instance.comment))
        instance.save()
        return instance
