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
