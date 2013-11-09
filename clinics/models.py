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
import cPickle as pickle
import os
import datetime

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
    

class PickleNotFoundException(Exception):
    """Missing Pickle Exception"""


class ClinicPickle(object):
    """Word dictionary utilities for pickling GRE words."""
    _PICKLE_FOLDER = os.path.join('data', 'clinics')
    _MISSING_PICKLE = 'Pickle {0} File Missing.'
    
    def __init__(self, name):
        self.name = name
        self.date_created = datetime.datetime.now()
    
    @classmethod
    def Create(cls, name):
        """Creates a clinic object and pickles it."""
        try:
            pickle_file_name = '{0}.pkl'.format(name)
            path_to_pickle = os.path.join(cls._PICKLE_FOLDER,
                                          pickle_file_name)
            path = os.path.isfile(path_to_pickle)
            if not path:
                pickle.dump(cls(name).__dict__, file(path_to_pickle, 'wb'))
        except IOError:
            raise PickleNotFoundException, self._MISSING_PICKLE.format(name)

    def Delete(self):
        """Deletes a Clinic Pickle File."""
        try:
            pickle_file_name = '{0}.pkl'.format(self.name)
            path_to_pickle = os.path.join(self._PICKLE_FOLDER,
                                          pickle_file_name)
            os.remove(path_to_pickle)
        except IOError:
            raise PickleNotFoundException, self._MISSING_PICKLE.format(name)

    @classmethod
    def GetAll(cls):
        return filter(lambda x: x != None, 
                      [cls.Load(name) for name in cls.GetAllClinicNames()])

    @classmethod
    def GetAllClinicNames(cls):
        pkl_files = [f for f in os.listdir(cls._PICKLE_FOLDER) 
                     if os.path.isfile(os.path.join(cls._PICKLE_FOLDER,f))]
        return [_.strip('.pkl') for _ in pkl_files]

    @classmethod
    def Load(cls, name):
        """Loads up a pickled clinic as a clinic object."""
        try:
            pickle_file_name = '{0}.pkl'.format(name)
            path_to_pickle = os.path.join(cls._PICKLE_FOLDER,
                                          pickle_file_name)
            if os.path.isfile(path_to_pickle):
                clinic = cls(name)
                clinic.__dict__ = pickle.load(file(path_to_pickle, 'r+b'))
            else:
                clinic = None
            return clinic
        except IOError:
            return None

    def Update(self, post_data):
        """Updates a clinic given the post_data dictionary."""
        self.__dict__.update({})
        try:
            pickle_file_name = '{0}.pkl'.format(self.name)
            path_to_pickle = os.path.join(self._PICKLE_FOLDER,
                                          pickle_file_name)
            if os.path.isfile(path_to_pickle):
                pickle.dump(self.__dict__, file(path_to_pickle), 'wb')
        except IOError:
            raise PickleNotFoundException, self._MISSING_PICKLE.format(name)
