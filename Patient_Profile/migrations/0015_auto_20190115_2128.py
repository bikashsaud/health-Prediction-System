# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-15 15:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Patient_Profile', '0014_auto_20190114_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='d_medical',
            name='amount',
            field=models.IntegerField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='d_medical',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 1, 15, 15, 43, 43, 233328, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='d_medical',
            name='follow_on_date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 15, 15, 43, 43, 233328, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='test_date',
            field=models.DateField(verbose_name=datetime.datetime(2019, 1, 15, 15, 43, 43, 233328, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 15, 15, 43, 43, 233328, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='test_result',
            name='test_date',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2019, 1, 15, 15, 43, 43, 233328, tzinfo=utc)),
        ),
    ]