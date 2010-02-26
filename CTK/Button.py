# CTK: Cherokee Toolkit
#
# Authors:
#      Alvaro Lopez Ortega <alvaro@alobbs.com>
#
# Copyright (C) 2009 Alvaro Lopez Ortega
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of version 2 of the GNU General Public
# License as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

from Widget import Widget

class Button (Widget):
    def __init__ (self, caption="Submit"):
        Widget.__init__ (self)

        self.id      = "button_%d" %(self.uniq_id)
        self.caption = caption

    # Public interface
    #
    def Render (self):
        id      = self.id
        caption = self.caption

        html = '<a id="%(id)s" href="#" class="button"><span>%(caption)s</span></a>' %(locals())

        render = Widget.Render (self)
        render.html += html

        return render
