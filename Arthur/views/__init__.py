# This file is part of Merlin/Arthur.
# Merlin/Arthur is the Copyright (C)2009,2010 of Elliot Rosemarine.

# Individual portions may be copyright by individual contributors, and
# are included in this collective work with permission of the copyright
# owners.

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
 
from django.conf.urls import include, patterns, url

urlpatterns = patterns('Arthur.views',
    (r'', include('Arthur.views.home')),
    (r'', include('Arthur.views.lookup')),
    (r'', include('Arthur.views.dashboard')),
    (r'', include('Arthur.views.members')),
    (r'', include('Arthur.views.planet')),
    (r'', include('Arthur.views.galaxy')),
    (r'', include('Arthur.views.alliance')),
    (r'', include('Arthur.views.search')),
    (r'', include('Arthur.views.exiles')),
    (r'', include('Arthur.views.attack')),
    (r'', include('Arthur.views.scans')),
    (r'', include('Arthur.views.graphs')),
)

from Arthur.views import home
from Arthur.views import dashboard
from Arthur.views import members
from Arthur.views import planet
from Arthur.views import galaxy
from Arthur.views import alliance
from Arthur.views import search
from Arthur.views import exiles
from Arthur.views import attack
from Arthur.views import scans
