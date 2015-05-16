# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtgs', '0004_mtg_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtg',
            name='twitter_tag',
            field=models.CharField(verbose_name='ツイッターハッシュタグ', null=True, blank=True, max_length=140),
            preserve_default=True,
        ),
    ]
