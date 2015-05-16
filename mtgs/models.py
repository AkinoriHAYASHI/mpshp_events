"""

(c) 2015 Morning Project Samurai

This file is part of mpsmtgs.
mps is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License.

mpsmtgs is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Building(models.Model):
    prefecture = models.CharField('都道府県', max_length=128, null=True, blank=True)
    address = models.CharField('住所', max_length=255, null=True, blank=True)
    name = models.CharField('名前', max_length=255, null=True, blank=True)

    hp_url = models.URLField('ホームページ', null=True, blank=True)
    map_url = models.URLField('地図', null=True, blank=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=128)

    building = models.ForeignKey(Building)

    hp_url = models.URLField('ホームページ', null=True, blank=True)
    map_url = models.URLField('建物案内図', null=True, blank=True)

    def __str__(self):
        return '%s%s' % (self.building, self.name)


class Mtg(models.Model):
    name = models.CharField('ミーティング名', max_length=128)
    number = models.PositiveIntegerField('回')

    start_time = models.DateTimeField('開始時刻')
    end_time = models.DateTimeField('終了時刻')
    due_time = models.DateTimeField('締め切り時刻')

    place = models.ForeignKey(Room, null=True, blank=True)

    organizers = models.ManyToManyField(User, related_name='mtg_organizers')
    members = models.ManyToManyField(User, related_name='mtg_members')

    max_members = models.PositiveIntegerField('最大人数')
    price = models.PositiveIntegerField('価格')

    hp_url = models.URLField('ホームページ', null=True, blank=True)

    detail = models.TextField('詳細')

    note = models.TextField('備考', null=True, blank=True)

    twitter_tag = models.CharField('ツイッターハッシュタグ', max_length=140, null=True, blank=True)

    report = models.TextField('事後報告', null=True, blank=True)

    def __str__(self):
        return '%s 第%s回' % (self.name, self.number)


class MtgHistory(models.Model):
    original = models.ForeignKey(Mtg)
    operator = models.ForeignKey(User, related_name='mtghistory_operator')
    operation = models.ForeignKey(User, related_name='mtghistory_operation')
    comment = models.TextField()
    reg_time = models.DateTimeField()

    name = models.CharField(max_length=128)
    time = models.DateTimeField()

    organizer = models.ManyToManyField(User, related_name='mtghistory_organizers')
    members = models.ManyToManyField(User, related_name='mtghistory_members')