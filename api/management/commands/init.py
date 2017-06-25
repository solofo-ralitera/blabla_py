# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from app.models.AttachmentType import AttachmentType
from app.models.PublicationType import PublicationType
from app.models.Attachment import Attachment
from app.models.Publication import Publication

from django.contrib.auth.models import User
from django.db import connection


class Command(BaseCommand):
    help = 'Init api'

    # def add_arguments(self, parser):
    #    parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        cursor = connection.cursor()

        cursor.execute('SET FOREIGN_KEY_CHECKS = 0')
        cursor.execute('TRUNCATE TABLE `{0}`'.format(Publication._meta.db_table))
        cursor.execute('TRUNCATE TABLE `{0}`'.format(Attachment._meta.db_table))
        cursor.execute('TRUNCATE TABLE `{0}`'.format(AttachmentType._meta.db_table))
        cursor.execute('TRUNCATE TABLE `{0}`'.format(PublicationType._meta.db_table))
        cursor.execute('TRUNCATE TABLE `{0}`'.format(User._meta.db_table))
        cursor.execute('SET FOREIGN_KEY_CHECKS = 1')

        attachment_types = [
            ['Text', 'TXT'],
            ['Link', 'LNK'],
            ['Picture', 'PCT'],
            ['Audio', 'AUD'],
            ['Video', 'VID'],
        ]
        for name, code in attachment_types:
            at = AttachmentType(name=name, code=code)
            at.save()

        publication_types = [
            ['Timeline', 'TML'],
            ['Comment', 'CMT'],
        ]
        for name, code in publication_types:
            pt = PublicationType(name=name, code=code)
            pt.save()

        admin = User.objects.create_user('admin', 'admin@blabla.com', 'admin')
        admin.is_superuser = 1
        admin.is_staff = 1
        admin.first_name = 'Admin'
        admin.last_name = 'Admin'
        admin.save()

        demo = User.objects.create_user('demo', 'demo@blabla.com', 'demo')
        demo.first_name = 'Demo'
        demo.last_name = 'Demo'
        demo.save()

        self.stdout.write(self.style.SUCCESS('Cmd successful'))

