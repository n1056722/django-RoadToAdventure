# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-21 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20170821_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupchat',
            name='Content',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]