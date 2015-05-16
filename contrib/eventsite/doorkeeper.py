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

import lxml.html
from . import base

class CommunityEventForm(base.EventForm):
    def _set_form(self):
        self._form = self._html.forms[0]

    def _fill_form(self):
        self._form.fields['event[title_ja]'] = self._event.name
        self._form.fields['event[starts_at_date]'] = self._event.start_date
        self._form.fields['event[starts_at_time(4i)]'] = self._event.start_hour
        self._form.fields['event[starts_at_time(5i)]'] = self._event.start_minute
        self._form.fields['event[ends_at_date]'] = self._event.end_date
        self._form.fields['event[ends_at_time(4i)]'] = self._event.end_hour
        self._form.fields['event[ends_at_time(5i)]'] = self._event.end_minute

        if self._event.price == 0 and self._event.prepaid_price == 0:
            self._form.fields['event[ticket_types_attributes][0][admission_type]'] = 'free'
        else:
            self._form.fields['event[ticket_types_attributes][0][admission_type]'] = 'paid'
            self._form.fields['event[ticket_types_attributes][0][door_admission_fee]'] = str(self._event.price)
            self._form.fields['event[ticket_types_attributes][0][prepaid_admission_fee]'] = str(self._event.prepaid_price)

        self._form.fields['event[ticket_types_attributes][0][available_until_type]'] = 'custom'
        self._form.fields['event[ticket_types_attributes][0][available_until_date]'] = self._event.due_date
        self._form.fields['event[ticket_types_attributes][0][available_until_time(4i)]'] = self._event.due_hour
        self._form.fields['event[ticket_types_attributes][0][available_until_time(5i)]'] = self._event.due_minute

        self._form.fields['event[admission_notes_ja]'] = self._event.note
        self._form.fields['event[ticket_limit]'] = str(self._event.max_members)
        self._form.fields['event[venue_name_ja]'] = '%s%s' % (self._event.building, self._event.room)
        self._form.fields['event[venue_url_ja]'] = '%s' % self._event.map_url
        self._form.fields['event[address_ja]'] = '%s%s%s%s' % (self._event.prefecture, self._event.address, self._event.building, self._event.room)

        self._form.fields['event[description_ja]'] = self._event.detail

        self._form.fields['event[hash_tag]'] = self._event.twitter_tag

def _test():
    event = base._create_test_event()

    form = CommunityEventForm(event)

    form._set_form()
    form._fill_form()

    return form