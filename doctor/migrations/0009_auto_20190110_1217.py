# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-10 06:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0008_auto_20190108_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='join_date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 10, 6, 32, 21, 90131, tzinfo=utc)),
        ),
    ]