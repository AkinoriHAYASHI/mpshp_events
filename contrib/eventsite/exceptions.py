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

class FormNotFound(Exception):
    pass

class MethodNotImplemented(Exception):
    def __init__(self, value=None):
        if value is None:
            self.msg = 'The method should be implemented.'
        else:
            self.msg = 'The method should be implemented and return %s.' % value

    def __str__(self):
        return repr(self.msg)