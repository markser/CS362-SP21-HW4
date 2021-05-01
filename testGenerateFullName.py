import io
import sys
import unittest
from unittest.mock import patch
import generateFullName
# run with python3 command 
# python3 testGenerateFullName.py
# had help with https://andressa.dev/2019-07-20-using-pach-to-test-inputs/

class TestCalculator(unittest.TestCase):
    @patch('builtins.input', side_effect=['foo','bar'])
    def test_first_and_last_name(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        generateFullName.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['Your full name is: foo bar ', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)
    
    @patch('builtins.input', side_effect=['foo', ''])
    def test_missing_last_name(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        generateFullName.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['missing firstname or lastname', '']
        actual = capturedOutput.getvalue().split('\n')
        print(actual)
        self.assertEqual(actual, expected)

        
    @patch('builtins.input', side_effect=['', 'bar'])
    def test_missing_first_name(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        generateFullName.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['missing firstname or lastname', '']
        actual = capturedOutput.getvalue().split('\n')
        print(actual)
        self.assertEqual(actual, expected)
    
    @patch('builtins.input', side_effect=['', ''])
    def test_both_missing(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        generateFullName.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['missing firstname or lastname', '']
        actual = capturedOutput.getvalue().split('\n')
        print(actual)
        self.assertEqual(actual, expected)
    
    @patch('builtins.input', side_effect=['123', '456'])
    def test_number_in_names(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        generateFullName.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['no integers in first or last name', '']
        actual = capturedOutput.getvalue().split('\n')
        print(actual)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()