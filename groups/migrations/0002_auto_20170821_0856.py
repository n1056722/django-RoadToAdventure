# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-21 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupChat',
            fields=[
                ('GroupChatID', models.AutoField(primary_key=True, serialize=False)),
                ('CreateDate', models.DateTimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='useringroup',
            old_name='UserInGroup',
            new_name='UserInGroupID',
        ),
        migrations.AlterField(
            model_name='group',
            name='CreateUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Group_CreateUser', to='users.UserAccount'),
        ),
        migrations.AlterField(
            model_name='group',
            name='ModifyUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Group_ModifyUser', to='users.UserAccount'),
        ),
        migrations.AlterField(
            model_name='useringroup',
            name='Group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='UserInGroup_Group', to='groups.Group'),
        ),
        migrations.AlterField(
            model_name='useringroup',
            name='GroupRole',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='UserInGroup_GroupRole', to='groups.GroupRole'),
        ),
        migrations.AlterField(
            model_name='useringroup',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='UserInGroup_User', to='users.UserAccount'),
        ),
        migrations.AddField(
            model_name='groupchat',
            name='Group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='GroupChat_Group', to='groups.Group'),
        ),
        migrations.AddField(
            model_name='groupchat',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='GroupChat_User', to='users.UserAccount'),
        ),
    ]