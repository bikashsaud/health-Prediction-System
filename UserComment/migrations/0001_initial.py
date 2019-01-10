# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-10 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('phoneno', models.IntegerField(blank=True)),
                ('comment', models.TextField()),
            ],
        ),
    ]