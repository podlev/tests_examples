# для запуска python3 -m doctest doctest_example -v
# или python3 doctest_example -v

def get_reversed_string(s):
    """
    Возвращает строку наоборот

    >>> get_reversed_string('123')
    '321'

    >>> get_reversed_string('')
    ''

    >>> get_reversed_string('111')
    '111'

    >>> get_reversed_string(123)
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not subscriptable
    """
    return s[::-1]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
