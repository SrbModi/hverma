# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-10 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0005_auto_20170301_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
