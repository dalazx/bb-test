import unittest

import anagram


class FindAnagramsTestCase(unittest.TestCase):
    def test_base(self):
        anagrams = anagram.find_anagrams(
            'abc', ('abc', 'bcd', 'test', 'cba', 'ab'))
        self.assertSetEqual(set(anagrams), {'abc', 'cba'})
