import unittest

import fizz_buzz


class GenerateFizzBuzzTestCase(unittest.TestCase):
    def test_base(self):
        fb = list(fizz_buzz.generate_fizz_buzz(xrange(1, 16)))
        self.assertListEqual(
            fb,
            ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz',
             '11', 'Fizz', '13', '14', 'FizzBuzz'])
