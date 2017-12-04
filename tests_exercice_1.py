import unittest
from exercice_1 import findNext
 
class TestUM(unittest.TestCase):
 
    def setUp(self):

        self.non_integer_test_matrix = [
            [1234.1, False],
            ["String", False],
            [False, False],
            ["", False],
            [None, False],
        ]

        self.positive_integer_test_matrix = [
            [0, 0],
            [1, 1],
            [120, 201],
            [132, 213],
            [1232, 1322],
            [4321, 4321],
            [7921, 9721],
            [7912, 7921],
            [1579, 1597],
            [9798, 9879],
        ]

        self.negative_integer_test_matrix = [
            [-0, -0],
            [-1, -1],
            [-4321, -3421],
        ]
 
    def test_non_integer_returns_false(self):
        for i in range(len(self.non_integer_test_matrix)): 
            self.assertEqual( findNext(self.non_integer_test_matrix[i][0]), self.non_integer_test_matrix[i][1])

    def test_positive_integer_returns_appropriate_number(self):
        for i in range(len(self.positive_integer_test_matrix)):    
            self.assertEqual( findNext(self.positive_integer_test_matrix[i][0]), self.positive_integer_test_matrix[i][1])

    def test_negative_integer_returns_appropriate_number(self):
        for i in range(len(self.negative_integer_test_matrix)):   
            self.assertEqual( findNext(self.negative_integer_test_matrix[i][0]), self.negative_integer_test_matrix[i][1])
 
if __name__ == '__main__':
    unittest.main()
