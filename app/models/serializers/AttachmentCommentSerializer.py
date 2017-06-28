# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from ..Attachment import Attachment, AttachmentComments
from ..Comment import Comment


class AttachmentCommentSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    attachment = serializers.ModelField(model_field=AttachmentComments()._meta.get_field('attachment'))
    comment = serializers.ModelField(model_field=AttachmentComments()._meta.get_field('comment'))

    class Meta:
        model = AttachmentComments
        fields = ('id', 'attachment', 'comment')

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
