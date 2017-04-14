# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airquality', '0002_auto_20170414_0603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='owners',
        ),
        migrations.AddField(
            model_name='alert',
            name='owners',
            field=models.CharField(default='', max_length=300),
        ),
    ]