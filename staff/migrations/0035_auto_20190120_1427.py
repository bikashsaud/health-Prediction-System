# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-20 08:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0034_auto_20190118_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='join_date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 20, 8, 41, 59, 154863, tzinfo=utc)),
        ),
    ]