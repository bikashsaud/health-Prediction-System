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
            name='superadmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneno', models.IntegerField(blank=True, default=0, null=True)),
                ('p_address', models.CharField(blank=True, default=0, max_length=300, null=True)),
                ('t_address', models.CharField(default=0, max_length=300)),
                ('sex', models.CharField(choices=[('M', 'male'), ('F', 'female')], default='M', max_length=2)),
                ('age', models.IntegerField(default=0)),
                ('post', models.CharField(default=0, max_length=30)),
                ('image', models.FileField(blank=True, upload_to='profilepicture')),
                ('cv', models.FileField(upload_to='cv/')),
                ('Portfolio', models.URLField(default=0)),
                ('degree', models.CharField(default=0, max_length=250)),
                ('university', models.CharField(default=0, max_length=100)),
                ('experience', models.IntegerField(default=0)),
                ('join_date', models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2019, 1, 1, 10, 2, 47, 41218, tzinfo=utc))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
