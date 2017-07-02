# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from app.models.Comment import Comment
from app.models.serializers.CommentSerializer import CommentSerializer
from .ApiView import View as ApiView


class View(ApiView):
    model = Comment
    serializer = CommentSerializer

    def __init__(self):
        super().__init__()
