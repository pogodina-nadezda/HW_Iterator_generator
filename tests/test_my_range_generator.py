import unittest

from my_range import MyRangeGenerator

class RangeGeneratorTests(unittest.TestCase):
    
    def test_iter_method(self):
        try:
            iter(MyRangeGenerator(5, 10, 3))
        except TypeError:
            print('It is not a generator')
             
    def test_range(self):
        list_range = [i for i in MyRangeGenerator(-5, 0, 3)]
        self.assertEqual(list_range, [-5, -2])