# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 17:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='sytle',
            new_name='style',
        ),
    ]
