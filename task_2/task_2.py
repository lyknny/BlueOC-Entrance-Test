"""
This is the 2nd task named Sum of Top Two Integers
Done by Linh Vu
"""
import heapq
import unittest

# Using this method will cause slower run times with O(n) time
def sum_of_top_two_int_without_heapq(lst):
    # Handling edge cases when list has less than 2 integers
    if len(lst) < 2:
        raise ValueError("This list should have at least two integers")

    # Initialize two variables to keep track of the maximum two numbers
    max_first = float('-inf')
    max_second = float('-inf')

    # Getting the two max numbers out of the list
    for num in lst:
        if num > max_first:
            max_second = max_first
            max_first = num
        elif num > max_second:
            max_second = num
    return max_first + max_second

# Using heap library to get the top two integers for better performance O(log(n))
def sum_of_top_two_int_with_heapq_library(lst):

    # Handling edge cases when list has less than 2 integers
    if len(lst) < 2:
        raise ValueError("This list should have at least two integers")

    top_two_numbers = heapq.nlargest(2, lst)
    return sum(top_two_numbers)

class TestSumOfTopTwoInteger(unittest.TestCase):

    # Test with the sample integers -> return the exact sum of the two biggest integers
    def test_with_sample_integers(self):
        result_1 = sum_of_top_two_int_without_heapq([1,4,2,3,5])
        result_2 = sum_of_top_two_int_with_heapq_library([1,4,2,3,5])
        expected = 9
        self.assertEqual(result_1, expected)
        self.assertEqual(result_2, expected)

    # Test with negative integers with summing of two biggest values    
    def test_with_negative_integers(self):
        result_1 = sum_of_top_two_int_without_heapq([-1,-4,-2,-3,-5])
        result_2 = sum_of_top_two_int_with_heapq_library([-1,-4,-2,-3,-5])
        expected = -3
        self.assertEqual(result_1, expected)
        self.assertEqual(result_2, expected)

    # Test with negative and positive integers with summing of two biggest values
    def test_with_negative_and_positive_integers(self):
        result_1 = sum_of_top_two_int_without_heapq([1,-4,2,-3,5])
        result_2 = sum_of_top_two_int_with_heapq_library([1,-4,2,-3,5])
        expected = 7
        self.assertEqual(result_1, expected)
        self.assertEqual(result_2, expected)
    
    # Test with rasing alarm of a list containing empty elements
    def test_raises_value_error_for_lacking_inputs(self):
        with self.assertRaises(ValueError):
            sum_of_top_two_int_without_heapq([])
        with self.assertRaises(ValueError):
            sum_of_top_two_int_with_heapq_library([])

    # Test with rasing alarm of a list containing one elements
    def test_raises_value_error_for_lacking_inputs(self):
        with self.assertRaises(ValueError):
            sum_of_top_two_int_without_heapq([1])
        with self.assertRaises(ValueError):
            sum_of_top_two_int_with_heapq_library([2])

if __name__ == '__main__':
    unittest.main()