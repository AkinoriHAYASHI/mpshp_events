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

__author__ = 'Junya Kaneko <junya@mpsamurai.org>'

from . import base
from . import exceptions

import re

class MonthFormat(base.MonthFormat):
    def get_month(self, datetime_obj):
        return str(datetime_obj.month)


class DayFormat(base.DayFormat):
    def get_day(self, datetime_obj):
        return str(datetime_obj.day)


class LoginForm(base.LoginForm):
    _base_url = 'https://mixi.jp'
    _path = ''

    def _set_form(self):
        self._form = self._html.forms[0]

    def _fill_form(self):
        self._form.fields['email'] = self._username
        self._form.fields['password'] = self._password


class LoginBirthdayForm(base.Form):
    _base_url = 'https://mixi.jp'
    _path = ''

    def __init__(self, year, month, day, opener=None, html_str=None, charset='euc-jp'):
        super(LoginBirthdayForm, self).__init__(opener, html_str, charset)
        self._year = year
        self._month = month
        self._day = day

    def _set_form(self):
        for form in self._html.forms:
            if form.fields['mode'] == "additional_auth_post":
                self._form = form
                return
        raise exceptions.FormNotFound()

    def _fill_form(self):
        self._form.fields['year'] = str(self._year)
        self._form.fields['month'] = str(self._month)
        self._form.fields['day'] = str(self._day)

class CommunityEventForm(base.EventForm):
    _base_url = 'http://mixi.jp'
    _path = ''

    _prefectures = {
        '北海道': 1,
        '青森県': 2,
        '岩手県': 3,
        '宮城県': 4,
        '秋田県': 5,
        '山形県': 6,
        '福島県': 7,
        '茨城県': 8,
        '栃木県': 9,
        '群馬県': 10,
        '埼玉県': 11,
        '千葉県': 12,
        '東京都': 13,
        '神奈川県': 14,
        '新潟県': 15,
        '富山県': 16,
        '石川県': 17,
        '福井県': 18,
        '山梨県': 19,
        '長野県': 20,
        '岐阜県': 21,
        '静岡県': 22,
        '愛知県': 23,
        '三重県': 24,
        '滋賀県': 25,
        '京都府': 26,
        '大阪府': 27,
        '兵庫県': 28,
        '奈良県': 29,
        '和歌山県': 30,
        '鳥取県': 31,
        '島根県': 32,
        '岡山県': 33,
        '広島県': 34,
        '山口県': 35,
        '徳島県': 36,
        '香川県': 37,
        '愛媛県': 38,
        '高知県': 39,
        '福岡県': 40,
        '佐賀県': 41,
        '長崎県': 42,
        '熊本県': 43,
        '大分県': 44,
        '宮崎県': 45,
        '鹿児島県': 46,
        '沖縄県': 47,
        }
    @property
    def community_id(self):
        return re.match(r'add_event.pl\?id=(\d+)', self._path).group(1)

    @community_id.setter
    def community_id(self, community_id):
        self._path = 'add_event.pl?id=%s' % community_id

    def _set_form(self):
        for form in self._html.forms:
            if 'submit' in form.fields and form.fields['submit'] == 'main':
                self._form = form
                return
        raise exceptions.FormNotFound()

    def _fill_form(self):
        self._event.month_format = MonthFormat()
        self._event.day_format = DayFormat()

        self._form.fields['title'] = self._event.name

        self._form.fields['start_year'] = self._event.start_year
        self._form.fields['start_month'] = self._event.start_month
        self._form.fields['start_day'] = self._event.start_day
        self._form.fields['start_note'] = '%s - %s' % (self._event.start_time, self._event.end_time)
        self._form.fields['location_pref_id'] = str(self._prefectures[self._event.prefecture])
        self._form.fields['location_note'] = '%s%s%s' % (self._event.address, self._event.building, self._event.room)
        self._form.fields['bbs_body'] = self._event.detail
        self._form.fields['deadline_year'] = self._event.due_year
        self._form.fields['deadline_month'] = self._event.due_month
        self._form.fields['deadline_day'] = self._event.due_day

    def submit(self, extra_values=None):
        if not self.community_id:
            raise exceptions.FormSubmissionFailuer('community_id must be specified.')
        else:
            return super(CommunityEventForm, self).submit(extra_values)


class CommunityEventConfirmationForm(CommunityEventForm):
    def _set_form(self):
        for form in self._html.forms:
            if 'submit' in form.fields and form.fields['submit'] == 'confirm':
                self._form = form
                return

    def _fill_form(self):
        pass