import unittest

"""
This is the 1st task named String Length Frequency using Python language
Done by Linh Vu
"""
# Indicates a list of most frequent length in a list of strings
def string_len_freq(lst):   
    # If the list is empty, no need to do anything, and return an empty list
    if len(lst) == 0:
        return []
    # Sorting a list by the length each string
    length_str = {length: [str for str in lst if len(str) == length] for length in set(len(str) for str in lst)}
    # Get a list of the most frequent occurrences of string length
    max_freq_length = max(length_str.values(), key=len)
    return max_freq_length

# Expected the print out a list with the most frequent length ['ab','cd','gh']
lst = ['a', 'ab','abc', 'cd','def','gh']
string_len_freq(lst)

class TestFreqStringLength(unittest.TestCase):

    # Test with an empty list -> return an empty list
    def test_empty_list(self):
        result = string_len_freq([])
        expected = []
        self.assertEqual(result, expected)

    # Test a single string -> return a single string
    def test_single_element(self):
        result = string_len_freq(['green'])
        expected = ['green']
        self.assertEqual(result, expected)

    # Test multiple strings with same length -> return all strings
    def test_single_occurrence(self):
        result = string_len_freq(['green', 'sport', 'roses', 'great', 'irony'])
        expected = ['green', 'sport', 'roses', 'great', 'irony']
        self.assertEqual(result, expected)

    # Test multiple strings with different lengths -> return the most frequent length
    def test_sample_occurrences_1(self):
        result = string_len_freq(['a', 'ab','abc', 'cd','def','gh'])
        expected =  ['ab','cd','gh']
        self.assertEqual(result, expected)
    
    # Test multiple strings with mixed lengths -> return the most frequent length
    def test_multiple_occurrences(self):
        result = string_len_freq(['pow', 'er','the', 'team','and','accelerate', 'the', 'speed'])
        expected =  ['pow','the','and', 'the']
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()