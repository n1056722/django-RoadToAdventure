# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 09:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='IsEnabled',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='IsVerification',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='LastLoginTime',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='LastPassword',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='UserPicture',
        ),
    ]
