# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-16 08:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0020_auto_20190116_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='join_date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 16, 8, 37, 47, 255586, tzinfo=utc)),
        ),
    ]