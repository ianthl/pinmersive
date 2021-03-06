# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-28 19:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('relationships', '0001_initial'),
        ('boards', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('avatar', models.ImageField(blank=True, upload_to=users.helpers.update_filename)),
                ('follows_boards', models.ManyToManyField(blank=True, through='relationships.UserFollowsBoard', to='boards.Board')),
                ('follows_users', models.ManyToManyField(blank=True, through='relationships.UserFollowsUser', to='users.UserProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
