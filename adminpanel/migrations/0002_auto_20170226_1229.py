# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-26 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='avail',
            field=models.BooleanField(),
        ),
    ]
