# -*- coding: utf-8 -*-

import pytest, os
from jool.utils import constant, cd

class _Constants(object):
    @constant
    def ANYTHING():
        return 'anything'

def test_get_constant():
    CONST = _Constants()
    assert CONST.ANYTHING == 'anything'

def test_set_constant():
    CONST = _Constants()
    with pytest.raises(TypeError):
        CONST.ANYTHING = 'assignment'

def test_change_directory():
    prev_dir = os.getcwd()
    with cd('/tmp/'):
        assert os.getcwd() == '/tmp' or os.getcwd() == '/private/tmp'

    assert os.getcwd() == prev_dir
