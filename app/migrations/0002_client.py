# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('nom_societe', models.CharField(max_length=50)),
            ],
        ),
    ]