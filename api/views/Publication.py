# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from app.models.Publication import Publication
from app.models.serializers.PublicationSerializer import PublicationSerializer
from .ApiView import View as ApiView


class View(ApiView):
    model = Publication
    serializer = PublicationSerializer

    def __init__(self):
        super().__init__()
