# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# http://jpadilla.com/post/73791304724/auth-with-json-web-tokens
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.models.AttachmentType import AttachmentType
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class RestrictedView(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication,)

    def get(self, request):
        data = []
        for at in AttachmentType.objects.all():
            data.append(at.to_array())
        return Response(data)

