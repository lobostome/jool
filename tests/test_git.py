# -*- coding: utf-8 -*-

from jool.git import BugFilter, FramePopulator, BugMap
from jool.data import Frame
from pygit2 import Repository
import os


def test_clone_repo(gitrepo):
    directory, g = gitrepo
    assert os.path.exists(g.repo_to)


def test_walk_repo(gitrepo):
    directory, g = gitrepo
    g.traverse()
    assert g.dataset.number_of_rows > 0
    assert g.dataset.number_of_columns == 8


def test_filter_has_bugs():
    f = BugFilter()
    bug = f.filter(['this', 'is', 'a', 'bug', 'with', 'fixes'])
    assert bug


def test_filter_no_bugs():
    f = BugFilter()
    bug = f.filter(['this', 'has', 'no', 'issues'])
    assert not bug


def test_populator_extract_key():
    populator = FramePopulator(Frame())

    value = 'commit_id'
    expected = 'id'
    assert populator.extract_key(value) == expected
    value = 'is_bug'
    expected = 'bug'
    assert populator.extract_key(value) == expected


def test_populator_create_transform_classname():
    populator = FramePopulator(Frame())

    value = 'author'
    expected = 'AuthorTransform'
    assert populator.create_transform_classname(value) == expected


def test_blame_mapper(gitrepo):
    directory, g = gitrepo
    repo = Repository("%s/jool/.git" % directory)
    commit = repo.revparse_single('9aeaac94cda9eb7e32d6f861079ab793a0311983')
    mapper = BugMap()
    assert mapper.map(
        repo,
        'c/d.py',
        5,
        commit) == '903b2d2c65f291492f30467edc6442b74a78ab92'
