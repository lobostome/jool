# -*- coding: utf-8 -*-

import os
from jool.directory import Location


def test_set_directory():
    location = Location()
    value = 'sthrandom'
    location.directory = value
    assert location.directory == value


def test_generate_temp_directory_name():
    location = Location()
    assert location.generate_temp_directory_name().startswith(
        "%s/%s" % (location.BASE_DIR, location.PREFIX))


def test_create_remove_temp_directory():
    location = Location()
    location.directory = location.generate_temp_directory_name()

    location.create_temp_directory()
    assert os.path.exists(location.directory)
    location.remove_temp_directory()
    assert not os.path.exists(location.directory)
