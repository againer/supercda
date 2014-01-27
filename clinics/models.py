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

import cPickle as pickle
import datetime
from lxml import etree
from lxml import objectify
import os

from django.core.urlresolvers import reverse
from django.db import models


class Clinic(models.Model):
    """Model for creating a clinic document."""
    confidentiality_code = models.CharField(max_length=28)
    confidentiality_display_name = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now=True)
    id_authority = models.CharField(max_length=28)
    id_extension = models.CharField(max_length=28)
    id_root = models.CharField(max_length=28)
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    def create_document_xml(self):
        """Creates XML representation of the clinic document."""
        document_header = self._create_document_header()
        document_body = self._create_document_body()

    def _create_document_body(self):
        """Creates the clinical document header (CCD style)."""
        clinical_document_compoents = self._get_document_components()
        return ''

    def _create_document_header(self):
        """Creates CDA compliant document header in XML."""
        return ''

    def _get_document_components(self):
        """Gets a list of all Clinic document components."""
        return []


class DocumentComponentBaseClass(models.Model):
    """Class for document components, such as vital sign components."""
    clinic = models.ForeignKey(Clinic)

    def to_xml(self):
        """Takes self.__dict__ and interpolates with xml representation."""
        raise NotImplementedError('DocumentComponent.to_xml')


class PlanOfCareComponent(DocumentComponentBaseClass):
    """Document component for indicating clinic care plans per patient.

    <component>
        <section>
            <templateId root="2.16.840.1.113883.10.20.22.2.10" />
            <code code="18776-5" codeSystem="2.16.840.1.113883.6.1"
                  codeSystemName="LOINC" displayName="Treatment plan" />
            <title>Plan of Care</title>
            <text>
                <paragraph>{text}</paragraph>
            </text>
        </section>
    </component>"""
    _CODE = {
        'code': '18776-6',
        'codeSystem': '2.16.840.1.113883.6.1',
        'codeSystemName': 'LOINC',
        'displayName': 'Treatment plan'
    }
    _TEMPLATE_ID = {'root': '2.16.840.1.113883.10.20.22.2.10'}
    _TITLE = 'Plan of Care'

    text = models.TextField()

    def to_xml(self):
        root = etree.Element('component')
        section = etree.SubElement(root, 'section')
        template_id = etree.SubElement(
            section,
            'templateId',
            **self._TEMPLATE_ID)
        code = etree.SubElement(
            section,
            'code',
            **self._CODE)
        title = etree.SubElement(
            section,
            'title',
            text=self._TITLE)
        text = etree.SubElement(section, 'text')
        paragraph = etree.SubElement(
            text,
            'paragraph',
            text=self.text or 'NA')
        return etree.tostring(root, pretty_print=True)
