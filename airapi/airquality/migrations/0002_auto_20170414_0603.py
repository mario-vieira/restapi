# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airquality', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='received',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
