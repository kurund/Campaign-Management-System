# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-15 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]