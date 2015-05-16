__author__ = 'Junya Kaneko <junya@mpsamurai.org>'

import lxml.html
from . import exceptions

from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode

class DateFormat:
    def get_date(self, datetime_obj):
        return datetime_obj.strftime('%Y-%m-%d')


class YearFormat:
    def get_year(self, datetime_obj):
        return datetime_obj.strftime('%Y')


class MonthFormat:
    def get_month(self, datetime_obj):
        return datetime_obj.strftime('%m')


class DayFormat:
    def get_day(self, datetime_obj):
        return datetime_obj.strftime('%d')


class TimeFormat:
    def get_time(self, datetime_obj):
        return datetime_obj.strftime('%H:%M')


class HourFormat:
    def get_hour(self, datetime_obj):
        return datetime_obj.strftime('%H')


class MinuteFormat:
    def get_minute(self, datetime_obj):
        return datetime_obj.strftime('%M')


class Event:
    date_format = DateFormat()
    year_format = YearFormat()
    month_format = MonthFormat()
    day_format = DayFormat()

    time_format = TimeFormat()
    hour_format = HourFormat()
    minute_format = MinuteFormat()

    def __init__(self, name='', start_datetime=None, end_datetime=None, due_datetime=None,
                 prefecture='', address='', building='', room='', map_url='', place_hp='',
                 organizers=[], members=[], max_members=15, price=0, prepaid_price=0,
                 hp_url='', detail='', note='', twitter_tag=''):

        self._name = name

        self._start_datetime = start_datetime
        self._end_datetime = end_datetime
        self._due_datetime = due_datetime

        self._prefecture = prefecture
        self._address = address
        self._building = building
        self._room = room
        self._map_url = map_url
        self._place_hp = place_hp

        self._organizers = organizers
        self._members = members
        self._max_members = max_members

        self._price = price
        self._prepaid_price = prepaid_price

        self._hp_url = hp_url
        self._detail = detail
        self._note = note
        self._twitter_tag = twitter_tag

    @property
    def name(self):
        return self._name

    @property
    def start_datetime(self):
        return self._start_datetime

    @property
    def start_date(self):
        return self.date_format.get_date(self._start_datetime)

    @property
    def start_year(self):
        return self.year_format.get_year(self._start_datetime)

    @property
    def start_month(self):
        return self.month_format.get_month(self._start_datetime)

    @property
    def start_day(self):
        return self.day_format.get_day(self._start_datetime)

    @property
    def start_time(self):
        return self.time_format.get_time(self._start_datetime)

    @property
    def start_hour(self):
        return self.hour_format.get_hour(self._start_datetime)

    @property
    def start_minute(self):
        return self.minute_format.get_minute(self._start_datetime)

    @property
    def end_datetime(self):
        return self._end_datetime

    @property
    def end_date(self):
        return self.date_format.get_date(self._end_datetime)

    @property
    def end_year(self):
        return self.year_format.get_year(self._end_datetime)

    @property
    def end_month(self):
        return self.month_format.get_month(self._end_datetime)

    @property
    def end_day(self):
        return self.day_format.get_day(self._end_datetime)

    @property
    def end_time(self):
        return self.time_format.get_time(self._end_datetime)

    @property
    def end_hour(self):
        return self.hour_format.get_hour(self._end_datetime)

    @property
    def end_minute(self):
        return self.minute_format.get_minute(self._end_datetime)

    @property
    def due_datetime(self):
        return self._due_datetime

    @property
    def due_date(self):
        return self.date_format.get_date(self._due_datetime)

    @property
    def due_year(self):
        return self.year_format.get_year(self._due_datetime)

    @property
    def due_month(self):
        return self.month_format.get_month(self._due_datetime)

    @property
    def due_day(self):
        return self.day_format.get_day(self._due_datetime)

    @property
    def due_time(self):
        return self.time_format.get_time(self._due_datetime)

    @property
    def due_hour(self):
        return self.hour_format.get_hour(self._due_datetime)

    @property
    def due_minute(self):
        return self.minute_format.get_minute(self._due_datetime)

    @property
    def note(self):
        return self._note

    @property
    def max_members(self):
        return self._max_members

    @property
    def prefecture(self):
        return self._prefecture

    @property
    def address(self):
        return self._address

    @property
    def building(self):
        return self._building

    @property
    def room(self):
        return self._room

    @property
    def map_url(self):
        return self._map_url

    @property
    def place_hp(self):
        return self._place_hp

    @property
    def price(self):
        return self._price

    @property
    def prepaid_price(self):
        return self._prepaid_price

    @property
    def hp_url(self):
        return self._hp_url

    @property
    def note(self):
        return self._note

    @property
    def detail(self):
        return self._detail

    @property
    def twitter_tag(self):
        return self._twitter_tag

class Form:
    _base_url = None
    _path = ''
    _charset = ''

    def __init__(self, opener=None, html_str=None, charset='utf-8'):
        if opener is None:
            cookiejar = CookieJar()
            self._opener = build_opener(HTTPCookieProcessor(cookiejar))
        else:
            self._opener = opener

        self._charset = charset

        self._html_str = html_str
        self._html = None
        self._form = None

    @property
    def charset(self):
        return self._charset

    @property
    def opener(self):
        return self._opener

    def _open_http(self, method, url, values):
        if method == 'GET':
            if '?' in url:
                url += '&'
            else:
                url += '?'
                url += urlencode(values)
            data = None
        else:
            data = urlencode(values).encode(self._charset)
        return self._opener.open(url, data)

    def _set_html(self):
        if self._base_url is None:
            raise ValueError('_base_url must be set.')

        if self._html_str is None:
            url = self._base_url + self._path
            response = self._opener.open(url)
            self._html_str = response.read()

        self._html = lxml.html.fromstring(self._html_str, self._base_url)
        if self._html.cssselect('meta[http-equiv="Content-Type"]'):
            self._charset = self._html.cssselect('meta[http-equiv="Content-Type"]')[0].get('content').split('charset=')[-1]

    def _set_form(self):
        raise exceptions.MethodNotImplemented()

    def _fill_form(self):
        raise exceptions.MethodNotImplemented()

    def submit(self, extra_values=None):
        self._set_html()
        self._set_form()
        self._fill_form()

        if self._form is None:
            raise exceptions.FormNotFound()
        else:
            return lxml.html.submit_form(self._form, extra_values, self._open_http)


class LoginForm(Form):
    def __init__(self, username, password, opener=None):
        super(LoginForm, self).__init__(opener)
        self._username = username
        self._password = password

class EventForm(Form):
    def __init__(self, event, opener=None):
        super(EventForm, self).__init__(opener)
        self._event = event


def _create_test_event():
    from datetime import datetime
    import pytz
    from mpsmtgs.settings import TIME_ZONE

    event_time = datetime(2015, 5, 24, 10, 0).replace(tzinfo=pytz.timezone(TIME_ZONE))

    event = Event(name='MPS', start_datetime=event_time, end_datetime=event_time, due_datetime=event_time,
                  prefecture='東京都', address='文京区', building='', room='', map_url='', place_hp='',
                  organizers=[], members=[], max_members=15, price=500,
                  hp_url='', detail='', note='', twitter_tag='')
    return event