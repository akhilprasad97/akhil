# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-05 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='xml',
            options={'ordering': ('title',)},
        ),
        migrations.RemoveField(
            model_name='xml',
            name='no',
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='xml',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
