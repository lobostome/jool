# -*- coding: utf-8 -*-

import os, shutil
from jool.directory import Location

def test_set_directory():
    l = Location()
    value = 'sthrandom'
    l.directory = value
    assert l.directory == value

def test_generate_temp_directory_name():
    l = Location()
    assert l.generate_temp_directory_name().startswith("%s/%s" % (l.BASE_DIR, l.PREFIX))

def test_create_remove_temp_directory():
    l = Location()
    l.directory = l.generate_temp_directory_name()

    l.create_temp_directory()
    assert os.path.exists(l.directory)
    l.remove_temp_directory()
    assert not os.path.exists(l.directory)
