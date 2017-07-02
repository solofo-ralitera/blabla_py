# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# http://jpadilla.com/post/73791304724/auth-with-json-web-tokens
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.http import Http404


class View(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication,)
    model = None
    serializer = None

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def save(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, object_id=None):
        if object_id is None or object_id == '':
            return Response(
                self.serializer(self.model.objects.all(), many=True).data
            )
        else:
            return Response(
                self.serializer(self.model.objects.get(pk=object_id), many=False).data
            )

    def post(self, request):
        return Response(
            self.save(self.serializer(data=request.data)),
            status=status.HTTP_201_CREATED
        )

    def put(self, request, object_id=None):
        return Response(self.save(
            self.serializer(
                self.get_object(pk=request.data['id']),
                data=request.data
            )
        ), status=status.HTTP_200_OK)

    def delete(self, request):
        self.get_object(pk=request.data['id']).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
