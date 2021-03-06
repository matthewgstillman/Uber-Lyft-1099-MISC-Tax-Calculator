# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-30 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UberTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField(default=2017)),
                ('start_hour', models.IntegerField()),
                ('start_minute', models.IntegerField()),
                ('am_pm', models.CharField(max_length=2)),
                ('start_address', models.TextField(max_length=200)),
                ('end_address', models.TextField(max_length=200)),
                ('fare', models.FloatField()),
                ('miles_driven', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
