# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-18 07:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0028_auto_20190118_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='join_date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 18, 7, 56, 1, 691467, tzinfo=utc)),
        ),
    ]
