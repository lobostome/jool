# -*- coding: utf-8 -*-

import os
import pytest
from jool.utils import cd
from jool.directory import Location
from jool.git import Git


@pytest.fixture()
def gitrepo():
    test_repo = "git@github.com:requests/requests.git"
    cloned_repo = "requests"
    location = Location()
    location.directory = location.generate_temp_directory_name()
    try:
        location.create_temp_directory()

        g = Git(os.environ['JOOL_PUBLIC_KEY'], os.environ['JOOL_PRIVATE_KEY'])
        with cd(location.directory):
            g.clone_repo(test_repo, cloned_repo)
            yield location.directory, g
    finally:
        location.remove_temp_directory()
