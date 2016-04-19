import unittest
import mldcalc

class MLDCalcTest(unittest.TestCase):

    def test_num_ints(self):
        """
        Correctly calculates the total number of integers
        stored in the specified file.
        """
        with open('testfile.csv', 'w') as testfile:
            lines = testfile.write('45,23,16,89,102,23,14')

        num_ints = num_ints_from_file('testfile.csv')
        self.assertEqual(num_ints, 10)

    def test_num_ints_multiline(self):
        """
        Correctly calculates the total number of integers stored in
        the specified file when the file contains multiple lines.
        """
        num_ints = num_ints_from_file('10_ints_multiline.csv')
        self.assertEqual(num_ints, 10)

    def test_num_ints_empty_file(self):
        """
        Correctly calculates the total number of integers stored in an empty
        file (i.e. 0)
        """
        num_ints = num_ints_from_file('empty.csv')
        self.assertEqual(num_ints, 0)

    def test_num_ints_non_integers(self):
        """
        Correctly handles the presence of non-integer values
        TODO: Find out how to handle non-integers
        """

    def test_mean_ints(self):
        """
        Correctly calculates the mean of integers stored in the specified file.
        """

    def test_mean_ints_empty_file(self):
        """
        Correctly returns an error if the specified file is empty.
        TODO: Should it return an error?
        """

    def test_highest_single_line(self):
        """
        Correctly calculates the number of integers in the line with the most
        integers in the specified file.
        """

    def test_most_common_integer(self):
        """
        Correctly calculates the integer that appears the most times in the
        specified file.
        """

    def test_most_common_integer_equal(self):
        """
        Correctly calculates the integer that appears the most times if more
        than one integer appears the same number of times.
        TODO: Figure out what to do here, return the last one appearing in the
        sequence or return an array? 
        """
