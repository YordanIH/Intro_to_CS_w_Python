import unittest
import temperature

class TestAboveFreezing(unittest.TestCase):
    """Tests for temperature.above_freezing."""

    def test_above_freezing_above(self):
        """Test a temperature that is above freezing."""

        expected = True
        actual = temperature.above_freezing_v2(5.2)
        self.assertEqual(expected, actual,"Temperature is above freezing")

    def test_above_freezing_below(self):

        """Test a temperature that is below freezing."""

        expected = False
        actual = temperature.above_freezing_v2(-2)
        self.assertEqual(expected, actual, "The temperature is below freezing")

    def test_above_freezing_at_zero(self):
        """Test a temperature that is at freezing."""

        expected = False
        actual = temperature.above_freezing_v2(0)
        self.assertEqual(expected, actual,"The temperature is at the freezing mark.")

unittest.main()
