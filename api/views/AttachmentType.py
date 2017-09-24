# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from app.models.AttachmentType import AttachmentType, AttachmentTypeSerializer
from .ApiView import View as ApiView


class View(ApiView):
    model = AttachmentType
    serializer = AttachmentTypeSerializer

    def __init__(self):
        super().__init__()
