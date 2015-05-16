# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtgs', '0003_auto_20150502_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtg',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='備考'),
            preserve_default=True,
        ),
    ]
