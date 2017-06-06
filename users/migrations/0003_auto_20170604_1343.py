# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-04 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='/pinmersive/static/images/default-avatar.png', upload_to='user_profile_avatars/'),
        ),
    ]