# -*- coding: utf-8 -*-

import os
from contextlib import contextmanager


def constant(f):
    def fset(self, value):
        raise TypeError

    def fget(self):
        return f()
    return property(fget, fset)


@contextmanager
def cd(new_dir):
    prev_dir = os.getcwd()
    try:
        os.chdir(os.path.expanduser(new_dir))
        yield
    finally:
        os.chdir(prev_dir)


class FramePopulator(object):
    def __init__(self, frame):
        self.lists = {}
        self.frame = frame
        self.variables = ['commit_id', 'commit_message', 'commit_author']
        for variable in self.variables:
            self.lists[variable] = []

    def create_lists(self, commit):
        for variable in self.variables:
            key = self.extract_key(variable)
            value = getattr(commit, key)
            if key == 'author':
                value = value.name
            self.lists[variable].append(value)

    def to_frame(self):
        for variable in self.variables:
            self.frame.add_column(variable, self.lists[variable])

    def extract_key(self, index):
        return index.split('_', maxsplit=1)[1]
