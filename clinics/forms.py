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
