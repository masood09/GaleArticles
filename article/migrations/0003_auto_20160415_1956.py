# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20160415_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(editable=False, max_length=255, unique=True),
        ),
    ]
