# -*- coding: utf-8 -*-

import os, pytest
from jool.utils import cd
from jool.directory import Location
from jool.git import Git

def test_clone_repo():
    test_repo = "git@github.com:requests/requests.git"
    try:
        l = Location()
        l.directory = l.generate_temp_directory_name()
        l.create_temp_directory()

        g = Git()
        with cd(l.directory):
            g.clone_repository(test_repo)
    finally:
        l.remove_temp_directory()
