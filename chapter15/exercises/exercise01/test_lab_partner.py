import unittest
import lab_partner 

class TestRunningSum(unittest.TestCase):
    """Tests for lab_partner.double_preceding."""

    def test_double_preceding_empty(self):
        """Test an empty list."""
        argument = []
        expected = []
        lab_partner.double_preceding(argument)
        self.assertEqual(expected, argument, "The list is empty.")

    def test_double_preceding_one_item(self):
        """Test a one item list"""

        argument = [5]
        expected = [0]
        lab_partner.double_preceding(argument)
        self.assertEqual(expected, argument, "The list contains one item.")

    def test_double_preceding_two_items(self):
        argument = [2, 5]
        expected = [0, 4]
        lab_partner.double_preceding(argument)
        self.assertEqual(expected, argument, "The list contains two items.")

    def test_double_preceding_multi_negative(self): 
        """Test a list of negative values."""
        argument = [-1, -5, -3, -4]
        expected = [0, -2, -10, -6] 
        lab_partner.double_preceding(argument) 
        self.assertEqual(expected, argument,"The list contains only negative values.")      

    def test_double_preceding_multi_zeros(self):
        """Test a list of zeros."""
        argument = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        lab_partner.double_preceding(argument)
        self.assertEqual(expected, argument, "The list contains only zeros.")
    def test_double_preceding_multi_positive(self): 
        """Test a list of positive values."""
        argument = [4, 2, 3, 6]
        expected = [0, 8, 4, 6] 
        lab_partner.double_preceding(argument) 
        self.assertEqual(expected, argument,"The list contains only positive values.")
    def test_double_preceding_multi_mix(self):
        """Test a list containing mixture of negative values, zeros and positive values."""
        argument = [4, 0, 2, -5, 0]
        expected = [0, 8, 0, 4, -10] 
        lab_partner.double_preceding(argument) 
        self.assertEqual(expected, argument,"The list contains a mixture of negative values, zeros and" + "positive values.")

unittest.main()  