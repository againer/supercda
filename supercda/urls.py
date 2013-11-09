"""
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

__author__      = "Alex Gainer (superrawr@gmail.com)"
__copyright__   = "Copyright 2013, Health Records For Everyone (HR4E)"

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from clinics.views import ClinicCreateView
from clinics.views import ClinicDeleteView
from clinics.views import ClinicListView
from clinics.views import ClinicUpdateView

from supercda.views import HomeView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^clinics/clinic/delete/(?P<slug>[a-zA-Z0-9-]+)/$', 
        ClinicDeleteView.as_view(template_name='clinics/clinic_delete.html'),
        name='clinic_detail'),
    url(r'clinics/clinic/edit/(?P<slug>[a-zA-Z0-9-]+)/$', 
        ClinicUpdateView.as_view(template_name='clinics/clinic_update.html'),
        name='clinic_update'),
    url(r'clinics/create/$', 
        ClinicCreateView.as_view(template_name='clinics/clinic_create.html'),
        name='clinic_create'),
    url(r'clinics/', 
        ClinicListView.as_view(template_name='clinics/clinics.html'),
        name='clinic_list'),
    url(r'^$', HomeView.as_view(template_name='index.html')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
