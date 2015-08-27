import unittest
import mock

import lru_cache


class LRUCacheTestCase(unittest.TestCase):
    def setUp(self):
        function = mock.Mock()
        function.__name__ = 'function'
        self.function = function

    def test_args(self):
        function = self.function
        wrapper = lru_cache.lru_cache()(function)
        function.return_value = 1

        value = wrapper(1)
        self.assertEqual(value, 1)
        function.assert_called_once_with(1)

        value = wrapper(1)
        self.assertEqual(value, 1)
        function.assert_called_once_with(1)
        function.assert_has_calls([mock.call(1)])

        function.return_value = 2
        value = wrapper(2)
        self.assertEqual(value, 2)
        function.assert_called_with(2)
        function.assert_has_calls([mock.call(1), mock.call(2)])

    def test_kwargs(self):
        function = self.function
        wrapper = lru_cache.lru_cache()(function)
        function.return_value = 1

        value = wrapper(a=1, b=2)
        self.assertEqual(value, 1)
        function.assert_called_once_with(a=1, b=2)

        value = wrapper(b=2, a=1)
        self.assertEqual(value, 1)
        function.assert_has_calls([mock.call(a=1, b=2)])

        function.return_value = 2
        value = wrapper(c=1, b=2)
        self.assertEqual(value, 2)
        function.assert_called_with(c=1, b=2)
        function.assert_has_calls([mock.call(a=1, b=2), mock.call(c=1, b=2)])

    def test_lru(self):
        function = self.function
        wrapper = lru_cache.lru_cache(max_size=3)(function)
        # queue: []

        function.return_value = 1
        value = wrapper(1)
        function.assert_has_calls([mock.call(1)])
        # queue: [1]

        function.return_value = 2
        value = wrapper(2)
        function.assert_has_calls([mock.call(1), mock.call(2)])
        # queue: [1, 2]

        function.return_value = 3
        value = wrapper(3)
        function.assert_has_calls([mock.call(1), mock.call(2), mock.call(3)])
        # queue: [1, 2, 3]

        function.return_value = 4
        value = wrapper(4)
        function.assert_has_calls([
            mock.call(1), mock.call(2), mock.call(3),
            mock.call(4)])
        # queue: [2, 3, 4]

        function.return_value = 1
        value = wrapper(1)
        function.assert_has_calls([
            mock.call(1), mock.call(2), mock.call(3),
            mock.call(4), mock.call(1)])
        # queue: [3, 4, 1]

        function.return_value = 3
        value = wrapper(3)
        function.assert_has_calls([
            mock.call(1), mock.call(2), mock.call(3),
            mock.call(4), mock.call(1)])
        # queue: [4, 1, 3]

        function.return_value = 2
        value = wrapper(2)
        function.assert_has_calls([
            mock.call(1), mock.call(2), mock.call(3),
            mock.call(4), mock.call(1), mock.call(2)])
        # queue: [1, 3, 2]

        function.return_value = 4
        value = wrapper(4)
        function.assert_has_calls([
            mock.call(1), mock.call(2), mock.call(3),
            mock.call(4), mock.call(1), mock.call(2),
            mock.call(4)])
        # queue: [3, 2, 4]
