# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-16 13:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0022_auto_20190116_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical',
            name='join_date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 16, 13, 16, 28, 93675, tzinfo=utc)),
        ),
    ]
