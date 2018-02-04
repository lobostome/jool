# -*- coding: utf-8 -*-

import os

def test_clone_repo(gitrepo):
    directory, test_repo, cloned_repo = gitrepo
    assert os.path.exists(cloned_repo)
