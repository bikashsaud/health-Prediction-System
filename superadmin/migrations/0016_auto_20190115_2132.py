# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-15 15:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0015_auto_20190115_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superadmin',
            name='join_date',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2019, 1, 15, 15, 47, 17, 196371, tzinfo=utc)),
        ),
    ]
