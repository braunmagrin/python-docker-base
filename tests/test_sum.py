import pytest
import fix_tests_pypath
import main


def test_sum():
    assert main.sum(0,0) == 0
    assert main.sum(0,1) == 1
    assert main.sum(1,0) == 1
    assert main.sum(1,1) == 2
