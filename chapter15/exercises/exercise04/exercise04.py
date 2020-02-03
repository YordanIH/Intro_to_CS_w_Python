import unittest
import TestSorting

class test_is_sorted(unitest.TestCase):

    def test_if_empty(self):
        argument = is_sorted([])
        expected = True
        self.assertEqual(expected, argument, 'Argument is empty string.')

    def test_with_one(self):
        argument = is_sorted([1])
        expected = True
        self.assertEqual(expected, argument, '')
    
    def test_repeating(self):
        argument = is_sorted([1,2,3,3,5])
        expected = True
        self.assertEqual(expected, argument, '')

    def test__with_one_wrong(self):
        argument = is_sorted([1,2,3,4,-100])
        expected = False
        self.assertEqual(expected, argument, '')

    def test_unsorted(self):
        argument = is_sorted(4,3,5,3])
        expected = False
        self.assertEqual(expected, argument, '')

unittest.main()