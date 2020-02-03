from TestPrefixes import all_prefixes
import unittest

class Test(unittest.TestCase):

    def test_for_empty_string(self):
        argument = all_prefixes('')
        expected = set()
        self.assertEqual(expected, argument, 'Argument is empty string.')

    def test_single_char(self):
        argument = all_prefixes('a')
        expected = {'a'}
        self.assertEqual(expected, argument, 'Argument has one character.')
    
    def test_a_single_word(self):
        argument = all_prefixes('finger')
        expected = {'f','fi','fin','fing','finge','finger'}
        self.assertEqual(expected, argument, 'Argument with four letter all are different.')

    def test_repeating_characters(self):
        argument = all_prefixes('laptop')
        expected = {'l','ls','lap','lapt','lapto','laptop','p'}
        self.assertEqual(expected, argument, 'Argument with four letter all are different.')

unittest.main()