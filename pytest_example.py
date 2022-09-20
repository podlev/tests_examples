# для запуска pytest pytest_example.py -v

import pytest


def get_reversed_string(s):
    return s[::-1]


def test_get_reversed_string():
    """
    Проверка строки
    """
    test_cases = [
        ('123', '321'),
        ('abc', 'cba'),
        ('Abc', 'cbA'),
        ('aaa', 'aaa')
    ]
    for string, expected in test_cases:
        assert get_reversed_string(string) == expected


def test_get_reversed_empty_string():
    """
    Проверка пустой строки
    """
    string = ''
    expected = ''
    assert get_reversed_string(string) == expected


def test_get_reversed_number():
    """
    Проверка числа
    """
    string = 123
    with pytest.raises(TypeError):
        get_reversed_string(string)
