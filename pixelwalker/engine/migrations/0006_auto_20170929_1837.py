# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0005_auto_20170927_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='average_bitrate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='media',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='media',
            name='width',
            field=models.IntegerField(null=True),
        ),
    ]