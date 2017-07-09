# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import errno
import json

from django.http import HttpResponse
from app.models.Attachment import Attachment
from app.models.serializers.AttachmentSerializer import AttachmentSerializer
from .ApiView import View as ApiView
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings


class View(ApiView):
    model = Attachment
    serializer = AttachmentSerializer

    def __init__(self):
        super().__init__()

    def get(self, request, object_id=None):
        if object_id is None or object_id == '':
            return super().get(request, object_id)
        else:
            attachment = self.get_object(pk=object_id)
            # Return image
            if attachment.type.code == 'PCT':
                parameters = json.loads(attachment.parameters)
                path = parameters.get(
                    'path',
                    os.path.join(settings.MEDIA_ROOT, '.'.join((str(attachment.id), parameters.get('extension', ''))))
                )
                with open(path, 'rb') as f:
                    return HttpResponse(f.read(), content_type=parameters.get('content_type', ''))
            else:
                return super().get(request, object_id)

    def put(self, request, attachment_id=None):
        return self.post(request, attachment_id=attachment_id)

    def post(self, request, attachment_id=None):
        if not attachment_id:
            attachment_id = None
        file = request.data['file']
        tmp, extension = file.content_type.split('/')
        path = os.path.join(settings.MEDIA_ROOT, '.'.join((str(attachment_id), extension)))
        # Set parameters
        request.data['parameters'] = json.dumps({
            'original_name': file.name,
            'path': path,
            'content_type': file.content_type,
            'size': file.size,
            'extension': extension
        })
        # Call put parent
        if attachment_id is None:
            post_result = super().post(request=request, object_id=None)
        else:
            post_result = super().put(request=request, object_id=attachment_id)

        try:
            os.remove(path)
        except OSError as e:
            if e.errno != errno.ENOENT:
                raise
        default_storage.save(
            path,
            ContentFile(file.read())
        )
        return post_result
