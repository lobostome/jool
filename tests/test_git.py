# -*- coding: utf-8 -*-

from pygit2 import Repository
import os


def test_clone_repo(gitrepo):
    directory, g = gitrepo
    assert os.path.exists(g.repo_to)


def test_walk_repo(gitrepo):
    directory, g = gitrepo
    g.traverse()
    assert g.dataset.number_of_rows > 0
    assert g.dataset.number_of_columns == 3
