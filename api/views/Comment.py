# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# http://jpadilla.com/post/73791304724/auth-with-json-web-tokens
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.models.Comment import Comment
from app.models.serializers.CommentSerializer import CommentSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class View(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication,)

    @classmethod
    def get(cls, request):
        return Response(
            CommentSerializer(Comment.objects.all(), many=True).data
        )

    @classmethod
    def post(cls, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @classmethod
    def put(cls, request):
        serializer = CommentSerializer(
            Comment.objects.get(pk=request.data['id']),
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
