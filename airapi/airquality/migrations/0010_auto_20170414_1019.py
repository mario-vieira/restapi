# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airquality', '0009_auto_20170414_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='alert',
            name='owners',
            field=models.ManyToManyField(to='airquality.Person'),
        ),
    ]
