# -*- coding: utf-8 -*-

import os
import pytest
import shutil
import tarfile
from jool.utils import cd
from jool.directory import Location
from jool.git import Git


@pytest.fixture()
def gitrepo():
    test_repo = 'testrepo.git'
    test_repo_tar = "%s.tar" % test_repo
    test_repo_dir = os.path.dirname(os.path.realpath(__file__))
    cloned_repo = 'jool'

    location = Location()
    location.directory = location.generate_temp_directory_name()
    location.create_temp_directory()

    shutil.copyfile(
        src="%s/%s" % (test_repo_dir, test_repo_tar),
        dst="%s/%s" % (location.directory, test_repo_tar))

    try:
        with cd(location.directory):
            with tarfile.open(test_repo_tar) as tar:
                def is_within_directory(directory, target):
                    
                    abs_directory = os.path.abspath(directory)
                    abs_target = os.path.abspath(target)
                
                    prefix = os.path.commonprefix([abs_directory, abs_target])
                    
                    return prefix == abs_directory
                
                def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
                
                    for member in tar.getmembers():
                        member_path = os.path.join(path, member.name)
                        if not is_within_directory(path, member_path):
                            raise Exception("Attempted Path Traversal in Tar File")
                
                    tar.extractall(path, members, numeric_owner=numeric_owner) 
                    
                
                safe_extract(tar)

            g = Git(
                os.environ['JOOL_PUBLIC_KEY'],
                os.environ['JOOL_PRIVATE_KEY'])
            g.clone_repo(test_repo, cloned_repo)
            yield location.directory, g
    finally:
        location.remove_temp_directory()
