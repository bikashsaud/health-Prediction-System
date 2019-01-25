# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-18 07:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Patient_Profile', '0025_auto_20190117_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='d_lab',
            name='date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 18, 7, 11, 55, 113227, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='d_medical',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 1, 18, 7, 11, 55, 97606, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='d_medical',
            name='follow_on_date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 18, 7, 11, 55, 97606, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='d_medical',
            name='p_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 7, 11, 55, 97606, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='test_date',
            field=models.DateField(verbose_name=datetime.datetime(2019, 1, 18, 7, 11, 55, 113227, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 18, 7, 11, 55, 97606, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='test_result',
            name='test_date',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2019, 1, 18, 7, 11, 55, 113227, tzinfo=utc)),
        ),
    ]