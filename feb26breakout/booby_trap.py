import unittest

def is_balanced(code):
    """
            I - List of integers
            O - A list of 
            C - considerations
            E - edge cases
    """
    if len(code) % 2 == 0: 
        return False

    if len(code) % 2 == 0: 
        return False

    char_counts = {}
    for char in code: 
        char_counts[char] = char_counts.get(char, 0) + 1

    odd_count = 0
    for count in char_counts.values():
        if count % 2 != 0:
            odd_count += 1

    return odd_count == 1


class TestProcessData(unittest.TestCase):
    def test_example_1(self):
        # Example test case (replace with your specific tests)
        self.assertEqual(is_balanced("arghh"), True)


if __name__ == '__main__':
    unittest.main()