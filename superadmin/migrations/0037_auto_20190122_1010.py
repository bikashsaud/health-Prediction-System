# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-22 04:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0036_auto_20190120_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superadmin',
            name='join_date',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2019, 1, 22, 4, 25, 35, 208978, tzinfo=utc)),
        ),
    ]
