# -*- coding: utf-8 -*-

import os, uuid
from .utils import constant

class Location(object):

    def __init__(self, directory = None):
        self.directory = directory

    def generate_temp_directory(self):
        pass

    def generate_temp_directory_name(self):
        return "%s_%s" % (self.PREFIX, uuid.uuid1())

    def remote_temp_directory(self):
        pass

    @constant
    def PREFIX():
        return 'jool'
