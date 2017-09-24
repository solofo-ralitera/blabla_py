# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from app.models.Comment import Comment
from .ApiView import View as ApiView


class View(ApiView):
    model = Comment

    def __init__(self):
        super().__init__()

    def get(self, request, comment_id):
        return self.get_comments(request, comment_id)

    def post(self, request, comment_id):
        return self.post_comment(request, comment_id)
