# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-04 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20160922_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assignee_rating',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='beneficiary_rating',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
