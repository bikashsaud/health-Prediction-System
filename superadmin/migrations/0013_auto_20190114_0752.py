# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-14 02:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0012_auto_20190113_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superadmin',
            name='join_date',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2019, 1, 14, 2, 7, 37, 868244, tzinfo=utc)),
        ),
    ]
