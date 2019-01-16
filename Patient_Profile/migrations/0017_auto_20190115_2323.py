# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-15 17:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Patient_Profile', '0016_auto_20190115_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='d_lab',
            name='date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 15, 17, 38, 9, 909969, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='d_medical',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 1, 15, 17, 38, 9, 909969, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='d_medical',
            name='follow_on_date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 15, 17, 38, 9, 909969, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='test_date',
            field=models.DateField(verbose_name=datetime.datetime(2019, 1, 15, 17, 38, 9, 925622, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 15, 17, 38, 9, 909969, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='test_result',
            name='test_date',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2019, 1, 15, 17, 38, 9, 925622, tzinfo=utc)),
        ),
    ]