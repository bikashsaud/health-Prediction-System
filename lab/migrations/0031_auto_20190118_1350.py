# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-18 08:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0030_auto_20190118_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='join_date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 18, 8, 5, 14, 206561, tzinfo=utc)),
        ),
    ]
