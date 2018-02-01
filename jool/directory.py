# -*- coding: utf-8 -*-

import os, shutil, uuid
from .utils import constant

class Location(object):

    def __init__(self, directory = None):
        self._directory = directory

    def create_temp_directory(self):
        if not os.path.exists(self._directory):
            os.makedirs(self._directory)

    def generate_temp_directory_name(self):
        return "%s/%s_%s" % (self.BASE_DIR, self.PREFIX, uuid.uuid1())

    def remove_temp_directory(self):
        if os.path.exists(self._directory):
            shutil.rmtree(self._directory)

    @property
    def directory(self):
        return self._directory

    @directory.setter
    def directory(self, value):
        self._directory = value

    @directory.deleter
    def directory(self):
        del self._directory

    @constant
    def PREFIX():
        return 'jool'

    @constant
    def BASE_DIR():
        return '/tmp'
