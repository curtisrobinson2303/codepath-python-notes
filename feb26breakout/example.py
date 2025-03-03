import unittest

def count_words(words):
    """
    This is a docstring used for code comment blocks in python

    Understand: 
        I - Inputs
        O - Outputs
        C - Constraints/Considerations
        E - Edge Cases
        
    Plan: 
        Key Idea: Use a dictionary to track word counts. 
        Steps: 
            Initialize an empty dictionary 
            Interate through each word in input list 
                If word exists in dictions, 
                    increment its count
                Otherwise, 
                    add it to the dictionary with count of 1 
            Return the dictionary

    """
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

class TestCountWords(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_words([]), {})

    def test_single_word(self):
        self.assertEqual(count_words(["hello"]), {"hello": 1})

    def test_multiple_words(self):
        self.assertEqual(count_words(["hello", "world", "hello", "python"]), {"hello": 2, "world": 1, "python": 1})

    def test_case_sensitivity(self):
        self.assertEqual(count_words(["Hello", "hello", "WORLD", "world"]), {"Hello": 1, "hello": 1, "WORLD": 1, "world": 1})

if __name__ == '__main__':
    unittest.main()