# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from app.models.AppUser import AppUser
from app.models.serializers.AppUserSerializer import AppUserSerializer, AppUserToArray
from .ApiView import View as ApiView
from rest_framework.response import Response


class View(ApiView):
    model = AppUser
    serializer = AppUserToArray

    def __init__(self):
        super().__init__()

    def post(self, request, object_id=None):
        self.model = AppUser
        user = User.objects.create_user(
            username=request.data.get('username'),
            email=request.data.get('email'),
            password=request.data.get('password'),
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name'),
        )
        user.save()
        return Response(
            AppUserSerializer(AppUser.objects.get(pk=user.id), many=False).data
        )

    def delete(self, request, object_id=None):
        self.model = User
        return super(View, self).delete(request, object_id)
