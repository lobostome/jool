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


class final(type):
    def __init__(cls, name, bases, namespace):
        super(final, cls).__init__(name, bases, namespace)
        for klass in bases:
            if isinstance(klass, final):
                raise TypeError(str(klass.__name__) + " is final")


class Singleton(type):
    instance = None

    def __call__(cls, *args, **kw):
        if not cls.instance:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance
