# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-10 12:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0002_auto_20161002_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchiveUserAction',
            fields=[
                ('action_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actions.Action')),
            ],
            options={
                'abstract': False,
            },
            bases=('actions.action',),
        ),
    ]
