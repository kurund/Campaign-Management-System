# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-19 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_kits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='content_type',
            field=models.CharField(choices=[('TXT', 'Text'), ('IMG', 'Image'), ('VID', 'Video'), ('HTM', 'HTML')], default='TXT', max_length=3),
        ),
    ]