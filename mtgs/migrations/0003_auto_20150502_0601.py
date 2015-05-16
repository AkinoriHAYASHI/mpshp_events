# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtgs', '0002_auto_20150502_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtg',
            name='max_members',
            field=models.PositiveIntegerField(default=15, verbose_name='最大人数'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mtg',
            name='price',
            field=models.PositiveIntegerField(default=500, verbose_name='価格'),
            preserve_default=False,
        ),
    ]
