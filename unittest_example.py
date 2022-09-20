# для запуска python3 -m unittest unittest_example.py -v

import unittest


def get_reversed_string(s):
    return s[::-1]


class TestReverseString(unittest.TestCase):
    def test_get_reversed_string(self):
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
            self.assertEqual(get_reversed_string(string), expected)

    def test_get_reversed_empty_string(self):
        """
        Проверка пустой строки
        """
        string = ''
        expected = ''
        self.assertEqual(get_reversed_string(string), expected)

    def test_get_reversed_number(self):
        """
        Проверка числа
        """
        string = 123
        with self.assertRaises(TypeError):
            get_reversed_string(string)


if __name__ == '__main__':
    unittest.main()
