import io
import sys
import unittest
from unittest.mock import patch
import volumeOfCube
# run with python3 command 
# python3 testVolumeOfCube.py
# had help with https://stackoverflow.com/questions/18161330/using-unittest-mock-to-patch-input-in-python-3/37467870 and 

class TestCalculator(unittest.TestCase):
    @patch('builtins.input', return_value="6")
    def test_non_complex_numbers(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        volumeOfCube.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = "Volume of Cube: 18.0\n"
        actual = capturedOutput.getvalue()
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="1.02")
    def test_complex_numbers(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        volumeOfCube.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = "Volume of Cube: 3.06\n"
        actual = capturedOutput.getvalue()
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="-1")
    def test_negative_values(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        volumeOfCube.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = "Please enter a positive integer greater than 0\n"
        actual = capturedOutput.getvalue()
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="a")
    def test_string_input(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        volumeOfCube.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = "Please enter a integer \n"
        actual = capturedOutput.getvalue()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()