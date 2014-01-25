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

__author__ = "Alex Gainer (superrawr@gmail.com)"
__copyright__ = "Copyright 2014, Health Records For Everyone (HR4E)"

from django import forms
from models import Clinic

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ClinicCreateForm(forms.ModelForm):
    """Creates a clinic object"""
    def __init__(self, *args, **kwargs):
        super(ClinicCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('create', 'Create'))

    class Meta:
        model = Clinic
