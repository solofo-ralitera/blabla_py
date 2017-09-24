# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from app.models.PublicationType import PublicationType
from app.models.serializers.PublicationTypeSerializer import PublicationTypeSerializer
from .ApiView import View as ApiView


class View(ApiView):
    model = PublicationType
    serializer = PublicationTypeSerializer

    def __init__(self):
        super().__init__()
