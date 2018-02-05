# -*- coding: utf-8 -*-

import os

def test_clone_repo(gitrepo):
    directory, g = gitrepo
    assert os.path.exists(g.repo_to)

def test_walk_repo(gitrepo):
    directory, g = gitrepo
    assert len(g.traverse()) > 0
