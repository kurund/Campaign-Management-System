# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-09-17 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbmodels', '0004_iauser_hashvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='center',
            name='phoneNumber',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
