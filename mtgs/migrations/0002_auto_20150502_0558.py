# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mtgs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='building',
        ),
        migrations.RemoveField(
            model_name='mtg',
            name='time',
        ),
        migrations.AddField(
            model_name='mtg',
            name='end_time',
            field=models.DateTimeField(verbose_name='終了時刻', default=datetime.datetime(2015, 5, 2, 5, 58, 24, 737657, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mtg',
            name='start_time',
            field=models.DateTimeField(verbose_name='開始時刻', default=datetime.datetime(2015, 5, 2, 5, 58, 30, 273529, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='building',
            name='address',
            field=models.CharField(verbose_name='住所', null=True, max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='building',
            name='hp_url',
            field=models.URLField(verbose_name='ホームページ', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='building',
            name='map_url',
            field=models.URLField(verbose_name='地図', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='building',
            name='name',
            field=models.CharField(verbose_name='名前', null=True, max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='building',
            name='prefecture',
            field=models.CharField(verbose_name='都道府県', null=True, max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mtg',
            name='detail',
            field=models.TextField(verbose_name='詳細'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mtg',
            name='hp_url',
            field=models.URLField(verbose_name='ホームページ', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mtg',
            name='name',
            field=models.CharField(verbose_name='ミーティング名', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mtg',
            name='number',
            field=models.PositiveIntegerField(verbose_name='回'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mtg',
            name='report',
            field=models.TextField(verbose_name='事後報告', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='hp_url',
            field=models.URLField(verbose_name='ホームページ', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='map_url',
            field=models.URLField(verbose_name='建物案内図', null=True, blank=True),
            preserve_default=True,
        ),
    ]
