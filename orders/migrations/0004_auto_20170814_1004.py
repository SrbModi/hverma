# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-14 10:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_content_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_content',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='order_delivery',
            name='order_id',
        ),
    ]
