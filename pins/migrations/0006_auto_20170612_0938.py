# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-12 09:38
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0005_auto_20170608_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='image_file',
            field=models.ImageField(blank=True, upload_to='pin_images/'),
        ),
        migrations.AlterField(
            model_name='pin',
            name='image_url',
            field=models.URLField(blank=True, max_length=2000, validators=[django.core.validators.URLValidator()]),
        ),
    ]
