# -*- coding: utf-8 -*-

import pytest
from jool.utils import constant

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
