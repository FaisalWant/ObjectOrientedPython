# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-06-19 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=39.9, max_digits=10),
        ),
    ]
