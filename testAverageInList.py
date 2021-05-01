import io
import sys
import unittest
from unittest.mock import patch
import averageInList
# run with python3 command 
# python3 testAverageInList.py
# had help with https://andressa.dev/2019-07-20-using-pach-to-test-inputs/

class TestCalculator(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '2', 'a'])
    def test_normal_values(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        averageInList.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['This is the user input list: [1.0, 2.0]', 'This is the average of elements in the list: 1.5', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['1.0', '2.7', 'a'])
    def test_complex_values(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        averageInList.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['This is the user input list: [1.0, 2.7]', 'This is the average of elements in the list: 1.85', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['a'])
    def test_empty(self,mock_input):
        averageInList.main() 
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        averageInList.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['This is the user input list: []', 'This is the average of elements in the list: 0', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['0','0','0','0','0','a'])
    def test_divide_by_zero(self,mock_input):
        averageInList.main() 
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        averageInList.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['This is the user input list: []', 'This is the average of elements in the list: 0', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()