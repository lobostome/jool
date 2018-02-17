# -*- coding: utf-8 -*-

from jool.git import BugFilter
import os


def test_clone_repo(gitrepo):
    directory, g = gitrepo
    assert os.path.exists(g.repo_to)


def test_walk_repo(gitrepo):
    directory, g = gitrepo
    g.traverse()
    assert g.dataset.number_of_rows > 0
    assert g.dataset.number_of_columns == 4


def test_filter_has_bugs():
    f = BugFilter()
    value = f.filter(['this', 'is', 'a', 'bug', 'with', 'fixes'])
    assert value


def test_filter_no_bugs():
    f = BugFilter()
    value = f.filter(['this', 'has', 'no', 'issues'])
    assert not value
