# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 16:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('roles', models.TextField(null=True)),
                ('last_login', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('parameters', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.AppUser')),
            ],
        ),
        migrations.CreateModel(
            name='AttachmentComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('attachment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Attachment')),
            ],
        ),
        migrations.CreateModel(
            name='AttachmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.AppUser')),
            ],
        ),
        migrations.CreateModel(
            name='CommentComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Comment')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='app.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='app.AppUser')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='app.AppUser')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('lang', models.CharField(max_length=6)),
                ('attachments', models.ManyToManyField(to='app.Attachment')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.AppUser')),
            ],
        ),
        migrations.CreateModel(
            name='PublicationComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Comment')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Publication')),
            ],
        ),
        migrations.CreateModel(
            name='PublicationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='publication',
            name='comments',
            field=models.ManyToManyField(through='app.PublicationComments', to='app.Comment'),
        ),
        migrations.AddField(
            model_name='publication',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.PublicationType'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comments',
            field=models.ManyToManyField(through='app.CommentComments', to='app.Comment'),
        ),
        migrations.AddField(
            model_name='attachmentcomments',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Comment'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='comments',
            field=models.ManyToManyField(through='app.AttachmentComments', to='app.Comment'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.AttachmentType'),
        ),
    ]
