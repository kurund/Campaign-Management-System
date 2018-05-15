# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-02 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_kits', '0002_page_content_type'),
        ('user_profiles', '0003_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='training_kits_seen',
            field=models.ManyToManyField(blank=True, related_name='users_seen', to='training_kits.TrainingKit'),
        ),
    ]