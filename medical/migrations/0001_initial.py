# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-01 10:02
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='medical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneno', models.IntegerField(default=0)),
                ('temporary_address', models.CharField(max_length=30)),
                ('permanent_address', models.CharField(max_length=30)),
                ('sex', models.CharField(choices=[('M', 'male'), ('F', 'female')], default='M', max_length=2)),
                ('age', models.IntegerField(default=0)),
                ('post', models.CharField(max_length=30)),
                ('image', models.FileField(upload_to='profilepicture')),
                ('Portfolio', models.URLField(default=0)),
                ('join_date', models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 1, 10, 2, 47, 25594, tzinfo=utc))),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
