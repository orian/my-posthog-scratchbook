import unittest
from contextlib import contextmanager

from scratchbook.func_to_test import i_am_your_func


class TestCoolFunc(unittest.TestCase):
    @contextmanager
    def capture_names(self):
        names = []
        def new_func(orig_fn, name):
            names.append(name)
            return orig_fn(name)

        with i_am_your_func._temp_patch(new_func):
            yield names

    def test_i_am_your_func(self):
        s = 'hello world'
        self.assertEqual('you want some hello world?', i_am_your_func(s))

    def test_i_am_your_func2(self):
        s = 'hello world'
        with self.capture_names() as names:
            self.assertEqual('you want some ABC?', i_am_your_func('ABC'))
            self.assertListEqual(['ABC'], names)


if __name__ == '__main__':
    unittest.main()
