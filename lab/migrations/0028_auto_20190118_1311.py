# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-18 07:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0027_auto_20190118_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='join_date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 18, 7, 26, 23, 416672, tzinfo=utc)),
        ),
    ]
