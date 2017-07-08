# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from app.models.Comment import Comment
from app.models.serializers.CommentSerializer import CommentSerializer
from .ApiView import View as ApiView
from rest_framework.response import Response


class View(ApiView):
    model = Comment
    serializer = CommentSerializer

    def __init__(self):
        super().__init__()

    def get(self, request, comment_id):
        comments = []
        for comment in self.model.objects.all():
            comments.append(comment.to_array())
        return Response(comments)
