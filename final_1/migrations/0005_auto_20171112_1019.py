# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 04:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('final_1', '0004_auto_20171112_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='current',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='users',
            name='state',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='voltage',
            field=models.FloatField(default=0.0),
        ),
    ]