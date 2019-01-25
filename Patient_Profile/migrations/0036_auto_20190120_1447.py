# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-20 09:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Patient_Profile', '0035_auto_20190120_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='d_lab',
            name='date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 20, 9, 2, 56, 906783, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='d_medical',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 1, 20, 9, 2, 56, 906783, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='d_medical',
            name='follow_on_date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 20, 9, 2, 56, 906783, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='d_medical',
            name='medical',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medical.medical'),
        ),
        migrations.AlterField(
            model_name='d_medical',
            name='p_date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 1, 20, 9, 2, 56, 906783, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='test_date',
            field=models.DateField(verbose_name=datetime.datetime(2019, 1, 20, 9, 2, 56, 906783, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 20, 9, 2, 56, 891159, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='test_result',
            name='test_date',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2019, 1, 20, 9, 2, 56, 906783, tzinfo=utc)),
        ),
    ]