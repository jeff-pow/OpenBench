# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#   OpenBench is a chess engine testing framework authored by Andrew Grant.   #
#   <https://github.com/AndyGrant/OpenBench>           <andrew@grantnet.us>   #
#                                                                             #
#   OpenBench is free software: you can redistribute it and/or modify         #
#   it under the terms of the GNU General Public License as published by      #
#   the Free Software Foundation, either version 3 of the License, or         #
#   (at your option) any later version.                                       #
#                                                                             #
#   OpenBench is distributed in the hope that it will be useful,              #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#   GNU General Public License for more details.                              #
#                                                                             #
#   You should have received a copy of the GNU General Public License         #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import django.urls, OpenBench.views

urlpatterns = [

    # Links for account managment
    django.urls.path(r'register/', OpenBench.views.register),
    django.urls.path(r'login/', OpenBench.views.login),
    django.urls.path(r'logout/', OpenBench.views.logout),
    django.urls.path(r'profile/', OpenBench.views.profile),

    # Links for viewing test tables
    django.urls.path(r'index/', OpenBench.views.index),
    django.urls.path(r'index/<int:page>/', OpenBench.views.index),
    django.urls.path(r'greens/', OpenBench.views.greens),
    django.urls.path(r'greens/<int:page>/', OpenBench.views.greens),
    django.urls.path(r'search/', OpenBench.views.search),
    django.urls.path(r'user/<str:username>/', OpenBench.views.user),
    django.urls.path(r'user/<str:username>/<int:page>/', OpenBench.views.user),

    # Links for viewing general information tables
    django.urls.path(r'users/', OpenBench.views.users),
    django.urls.path(r'machines/', OpenBench.views.machines),
    django.urls.path(r'eventLog/', OpenBench.views.eventLog),
    django.urls.path(r'eventLog/<int:page>/', OpenBench.views.eventLog),

    # Links for viewing and managing tests (maintain Legacy)
    django.urls.path(r'test/<int:id>/', OpenBench.views.test),
    django.urls.path(r'viewTest/<int:id>/', OpenBench.views.test),
    django.urls.path(r'test/<int:id>/<str:action>', OpenBench.views.test),
    django.urls.path(r'newTest/', OpenBench.views.newTest),

    # Links for the Client to update the Server
    django.urls.path(r'getFiles/', OpenBench.views.getFiles),
    django.urls.path(r'getWorkload/', OpenBench.views.getWorkload),
    django.urls.path(r'wrongBench/', OpenBench.views.wrongBench),
    django.urls.path(r'submitNPS/', OpenBench.views.submitNPS),
    django.urls.path(r'submitResults/', OpenBench.views.submitResults),

    # Redirect anything else to the Index
    django.urls.path(r'', OpenBench.views.index),
]
