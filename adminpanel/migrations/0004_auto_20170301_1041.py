# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-01 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0003_imageslider'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='events',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='products',
            name='nut_1',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='nut_2',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='nut_3',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='nut_4',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='nut_5',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='short_desc',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='prod_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='prod_name',
            field=models.CharField(max_length=15),
        ),
    ]
