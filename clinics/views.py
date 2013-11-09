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


from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from models import ClinicPickle
from models import Clinic
from .forms import ClinicCreateForm


class ClinicActionMixin(object):
    """Action mixin class for Clinic manipulation."""
    
    @property
    def action(self):
        message = '{0} is missing action.'.format(self.__class__)
        raise NotImplementedError(message)
    
    def form_valid(self, form):
        message = 'Clinic {0}!'.format(self.action)
        messages.info(self.request, message)
        return super(ClinicActionMixin, self).form_valid(form)


class ClinicDeleteView(ClinicActionMixin, DeleteView):
    """View responsible for deleting Clinic objects."""
    model = Clinic
    action = 'deleted'
    success_url = reverse_lazy('clinic_list')


class ClinicCreateView(ClinicActionMixin, CreateView):
    """Creates a clinic provided a valid form submission is given."""
    model = Clinic
    action = 'created'
    form_class = ClinicCreateForm
    success_url = reverse_lazy('clinic_list')
    def form_invalid(self, form):
        return super(ClinicCreateView, self).form_invalid(form)


class ClinicListView(ListView):
    """View for viewing multiple clinics. Derp."""
    model = Clinic
    
    
class ClinicUpdateView(ClinicActionMixin, UpdateView):
    model = Clinic    

