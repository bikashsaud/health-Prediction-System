# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-13 05:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0011_auto_20190113_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical',
            name='join_date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 13, 5, 46, 35, 860334, tzinfo=utc)),
        ),
    ]