# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-26 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login_data',
            name='status',
            field=models.SmallIntegerField(default='0'),
        ),
    ]
