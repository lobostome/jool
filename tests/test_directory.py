# -*- coding: utf-8 -*-

from jool.directory import Location

def test_generate_temp_directory_name():
    l = Location()
    assert l.generate_temp_directory_name().startswith(l.PREFIX)
