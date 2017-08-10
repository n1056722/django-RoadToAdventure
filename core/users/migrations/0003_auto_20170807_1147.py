# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170725_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfriend',
            name='CreateUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='UserFriend_CreateUser', to='users.UserAccount'),
        ),
        migrations.AlterField(
            model_name='userfriend',
            name='FriendUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='UserFriend_FriendUser', to='users.UserAccount'),
        ),
    ]