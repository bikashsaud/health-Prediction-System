# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-18 08:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0031_auto_20190118_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superadmin',
            name='join_date',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2019, 1, 18, 8, 40, 52, 999601, tzinfo=utc)),
        ),
    ]
