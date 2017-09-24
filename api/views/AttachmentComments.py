# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from app.models.Attachment import Attachment
from .ApiView import View as ApiView


class View(ApiView):
    model = Attachment

    def __init__(self):
        super().__init__()

    def get(self, request, attachment_id=None):
        return self.get_comments(request, attachment_id)

    def post(self, request, attachment_id=None):
        return self.post_comment(request, attachment_id)

