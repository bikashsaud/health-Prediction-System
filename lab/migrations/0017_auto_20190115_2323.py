# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-15 17:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0016_auto_20190115_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='join_date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 15, 17, 38, 9, 894375, tzinfo=utc)),
        ),
    ]
