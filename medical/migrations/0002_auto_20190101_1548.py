# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-01 10:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical',
            name='join_date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 1, 10, 3, 10, 430740, tzinfo=utc)),
        ),
    ]