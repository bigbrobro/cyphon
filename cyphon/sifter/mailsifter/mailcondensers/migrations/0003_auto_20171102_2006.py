# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-02 20:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailcondensers', '0002_auto_20170623_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailcondenser',
            name='bottle',
            field=models.ForeignKey(help_text='The bottle (custom data model) into which the raw data will be distilled and stored.', on_delete=django.db.models.deletion.CASCADE, to='bottles.Bottle'),
        ),
    ]
