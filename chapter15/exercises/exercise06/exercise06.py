import unittest
from average import average

class test_average(unittest.TestCase):

    def test_with_two(self):
        argument=average([20,30])
        expected= 25
        self.assertEqual(expected, argument, 'List has only two values')

    def test_with_none(self):
        argument=average([20,30,None])
        expected= 25
        self.assertEqual(expected, argument, 'List has only two values and None')

    def test_with_two(self):
        argument=average([])
        expected= None
        self.assertEqual(expected, argument, 'Empty List')

unittest.main()