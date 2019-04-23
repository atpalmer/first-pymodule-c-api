import pytest
import first


def test_print_str():
    first.print_str('hello there, world!!!')


def test_print_int():
    first.print_int(1)


def test_print_int_bad_input():
    with pytest.raises(TypeError):
        first.print_int('invalid input')


def test_print_str_bad_input():
    with pytest.raises(TypeError):
        first.print_str(-1)
