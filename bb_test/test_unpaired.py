import unittest

import unpaired


class FindUnpairedNumberTestCase(unittest.TestCase):
    def test_base(self):
        number = unpaired.find_unpaired_number((5, 4, 1, 4, 3, 3, 2, 5, 2))
        self.assertEqual(number, 1)
