# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 05:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('final_1', '0006_auto_20171112_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='msg',
            name='date',
        ),
    ]
