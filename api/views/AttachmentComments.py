# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.response import Response
from app.models.Attachment import Attachment
from app.models.serializers.CommentSerializer import CommentSerializer
from .ApiView import View as ApiView


class View(ApiView):
    model = Attachment

    def __init__(self):
        super().__init__()

    def get(self, request, attachment_id):
        return Response(
            CommentSerializer(
                self.get_object(pk=attachment_id).get_comments(),
                many=True
            ).data
        )

    def post(self, request, attachment_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            self.get_object(pk=attachment_id).add_comment(serializer.save())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
