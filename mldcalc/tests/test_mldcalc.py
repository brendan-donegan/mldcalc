import unittest
from mldcalc import calc

def _write_to_file(ints):
    with open('testfile.csv', 'w') as testfile:
        testfile.write(ints)

class MLDCalcTest(unittest.TestCase):

    def test_num_ints(self):
        """
        Correctly calculates the total number of integers
        stored in the specified file.
        """
        _write_to_file('45,23,16,89,102,23,14')

        num_ints = calc.num_ints_from_file('testfile.csv')
        self.assertEqual(num_ints, 7)

    def test_num_ints_multiline(self):
        """
        Correctly calculates the total number of integers stored in
        the specified file when the file contains multiple lines.
        """
        _write_to_file('\n'.join(['45,23,16,89', '102,23,14']))
        num_ints = calc.num_ints_from_file('testfile.csv')
        self.assertEqual(num_ints, 7)

    def test_num_ints_empty_file(self):
        """
        Correctly calculates the total number of integers stored in an empty
        file (i.e. 0)
        """
        _write_to_file('')
        num_ints = calc.num_ints_from_file('testfile.csv')
        self.assertEqual(num_ints, 0)

    def test_num_ints_non_integers(self):
        """
        Correctly ignores non-integer values
        """
        _write_to_file('45,23,1b6,89')
        num_ints = calc.num_ints_from_file('testfile.csv')
        self.assertEqual(num_ints, 3)

    def test_mean_ints(self):
        """
        Correctly calculates the mean of integers stored in the specified file.
        """
        _write_to_file('45,23,16,89')
        mean = calc.mean_from_file('testfile.csv')
        self.assertEqual(mean, 43.25)

    def test_mean_ints_more_than_three_places(self):
        """
        Correctly returns a floating point number with three decimal places
        if there could be more than three.
        """
        _write_to_file('4,5,1')
        mean = calc.mean_from_file('testfile.csv')
        self.assertEqual(mean, 3.333)

    def test_mean_ints_empty_file(self):
        """
        Correctly returns None if the specified file is empty.
        """
        _write_to_file('')
        mean = calc.mean_from_file('testfile.csv')
        self.assertIsNone(mean)

    def test_mean_ints_invalid_integers(self):
        """
        Correctly returns None if the specified file contains invalid
        integers.
        """
        _write_to_file('45,23,1b6,78')
        mean = calc.mean_from_file('testfile.csv')
        self.assertEqual(mean, 48.667)

    def test_longest_line(self):
        """
        Correctly calculates the number of integers in the line with the most
        integers in the specified file.
        """
        _write_to_file('\n'.join([
                '45,20,34,56',
                '67,16,22',
                '90,17,22,40,23',
                '30'
            ]))
        longest = calc.longest_line_from_file('testfile.csv')
        self.assertEqual(longest, 5)

    def test_most_common_integer(self):
        """
        Correctly calculates the integer that appears the most times in the
        specified file.
        """
        _write_to_file('42,65,78,81,42,23,42')
        most_common = calc.most_common_from_file('testfile.csv')
        self.assertItemsEqual(most_common, [42])

    def test_most_common_integer_equal(self):
        """
        Correctly calculates the integers that appear the most times if more
        than one integer appears the same number of times.
        """
        _write_to_file('13,42,67,42,90,1,13')
        most_common = calc.most_common_from_file('testfile.csv')
        self.assertItemsEqual(most_common, [42,13])

    def test_most_common_integer_one_of_each(self):
        """
        Correctly returns all integers if they all occur an
        equal number of times.
        """
        _write_to_file('13,42,90,42,90,13')
        most_common = calc.most_common_from_file('testfile.csv')
        self.assertItemsEqual(most_common, [42, 90, 13])
