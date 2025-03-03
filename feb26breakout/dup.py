import unittest

from collections import Counter
def find_duplicate_chests(chests):
    """
            I - List of integers
            O - A list of 
            C - 
            E - Input list of size 0 or 1
        

            Plan: 
                Key Ideas:
                Steps: 
                    
            
    """
    freqs = Counter(chests)

    result = []

    sorted_dict = dict(sorted(freqs.items(), key=lambda item: int(item[0])))

    element = ""
    val = 0
    for element, val in sorted_dict.items(): 
        if val > 1: 
            result.append(element)
    return result
    
     
class TestCountWords(unittest.TestCase):
    def test1(self):
        self.assertEqual(find_duplicate_chests([4, 3, 2, 7, 8, 2, 3, 1]), [2, 3])
    def test2(self):
        self.assertEqual(find_duplicate_chests([1, 1, 2]), [1])
    def test3(self):
        self.assertEqual(find_duplicate_chests([1]), [])

if __name__ == '__main__':
    unittest.main()