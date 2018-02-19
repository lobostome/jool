# -*- coding: utf-8 -*-

from jool.git import BugFilter, FramePopulator
from jool.data import Frame
import os


def test_clone_repo(gitrepo):
    directory, g = gitrepo
    assert os.path.exists(g.repo_to)


def test_walk_repo(gitrepo):
    directory, g = gitrepo
    g.traverse()
    assert g.dataset.number_of_rows > 0
    assert g.dataset.number_of_columns == 6


def test_filter_has_bugs():
    f = BugFilter()
    value = f.filter(['this', 'is', 'a', 'bug', 'with', 'fixes'])
    assert value


def test_filter_no_bugs():
    f = BugFilter()
    value = f.filter(['this', 'has', 'no', 'issues'])
    assert not value


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
