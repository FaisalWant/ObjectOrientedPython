# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-06-12 12:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190612_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2019, 6, 12, 12, 6, 27, 572702, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postmodel',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
