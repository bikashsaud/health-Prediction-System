# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-16 13:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0022_auto_20190116_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='join_date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 16, 13, 16, 28, 78082, tzinfo=utc)),
        ),
    ]