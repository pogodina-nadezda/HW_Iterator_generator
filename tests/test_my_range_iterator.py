import unittest

from my_range import MyRange

class RangeIteratorTests(unittest.TestCase):
    
    def test_iter_method(self):
        try:
            iter(MyRange(5, 10, 3))
        except TypeError:
            print('It is not an iterator')
    
    def test_range(self):
        list_range = [i for i in MyRange(-5, 0, 3)]
        self.assertEqual(list_range, [-5, -2], '')