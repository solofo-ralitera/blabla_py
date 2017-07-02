# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from app.models.Attachment import Attachment
from app.models.serializers.AttachmentSerializer import AttachmentSerializer
from .ApiView import View as ApiView


class View(ApiView):
    model = Attachment
    serializer = AttachmentSerializer

    def __init__(self):
        super().__init__()
