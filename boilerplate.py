import unittest
from collections import Counter

def process_data(data):
    """
    I - Input data (type varies based on the problem)
    O - Processed output data (type varies based on the problem)
    C - Constraints (if any)
    E - Edge cases (if any)

    Plan: 
        Key Ideas:
            - Describe the core concepts and algorithms to be used.
        Steps: 
            1.  Outline the high-level steps of the process.
            2.  Detail each step with specific actions.
            3.  Handle any necessary data transformations.
            4.  Return the processed output.
    """
    # Placeholder for your data processing logic
    # Example using Counter (replace with your specific logic)
    if isinstance(data, list):
        freqs = Counter(data)
        result = []

        for item, count in freqs.items():
            if count > 1:
                result.append(item)

        result.sort()
        return result
    else:
        # Handle other data types or return a default value
        return None

class TestProcessData(unittest.TestCase):
    def test_example_1(self):
        # Example test case (replace with your specific tests)
        self.assertEqual(process_data([4, 3, 2, 7, 8, 2, 3, 1]), [2, 3])

    def test_example_2(self):
        # Example test case (replace with your specific tests)
        self.assertEqual(process_data([1, 1, 2]), [1])

    def test_empty_list(self):
        # Example test case (replace with your specific tests)
        self.assertEqual(process_data([]), [])

    def test_single_element_list(self):
        # Example test case (replace with your specific tests)
        self.assertEqual(process_data([1]), [])

    def test_other_data_type(self):
        # Example test case for handling other data types
        self.assertEqual(process_data("string"), None)

    def test_other_data_type_dict(self):
        self.assertEqual(process_data({"a":1}), None)

    def test_other_data_type_int(self):
        self.assertEqual(process_data(10), None)

if __name__ == '__main__':
    unittest.main()