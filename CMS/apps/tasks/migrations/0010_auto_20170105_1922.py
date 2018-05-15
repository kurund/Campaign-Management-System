# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-05 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_task_interests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='interests',
            field=models.ManyToManyField(related_name='tasks', to='interests.Interest'),
        ),
    ]