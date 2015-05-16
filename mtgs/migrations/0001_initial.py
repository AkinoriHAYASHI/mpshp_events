# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('prefecture', models.CharField(max_length=128, null=True, blank=True)),
                ('address', models.CharField(max_length=255, null=True, blank=True)),
                ('building', models.CharField(max_length=255, null=True, blank=True)),
                ('hp_url', models.URLField(null=True, blank=True)),
                ('map_url', models.URLField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mtg',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('number', models.PositiveIntegerField()),
                ('time', models.DateTimeField()),
                ('hp_url', models.URLField(null=True, blank=True)),
                ('detail', models.TextField()),
                ('report', models.TextField(null=True, blank=True)),
                ('members', models.ManyToManyField(related_name='mtg_members', to=settings.AUTH_USER_MODEL)),
                ('organizers', models.ManyToManyField(related_name='mtg_organizers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MtgHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('reg_time', models.DateTimeField()),
                ('name', models.CharField(max_length=128)),
                ('time', models.DateTimeField()),
                ('members', models.ManyToManyField(related_name='mtghistory_members', to=settings.AUTH_USER_MODEL)),
                ('operation', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='mtghistory_operation')),
                ('operator', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='mtghistory_operator')),
                ('organizer', models.ManyToManyField(related_name='mtghistory_organizers', to=settings.AUTH_USER_MODEL)),
                ('original', models.ForeignKey(to='mtgs.Mtg')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('hp_url', models.URLField(null=True, blank=True)),
                ('map_url', models.URLField(null=True, blank=True)),
                ('building', models.ForeignKey(to='mtgs.Building')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mtg',
            name='place',
            field=models.ForeignKey(null=True, to='mtgs.Room', blank=True),
            preserve_default=True,
        ),
    ]
