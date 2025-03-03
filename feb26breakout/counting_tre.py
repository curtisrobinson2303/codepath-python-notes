import unittest

def total_treasure(treasure_map):
    """
    I - treasure_map --> dict. with keys as strings and value as int
    O - print to console the total sum of all the values
    C - checking if empty map
    E - we get it

    Plan: 
        Key Ideas: using enum to grab all values 
        Steps:
            Define total treasures
            iterate through treasure_map with for loop 
            access key value pairs through .first and .second
            sum values to total global sum variable
    """

    sum = 0
    for key, val in treasure_map.items():
        sum += val

    return sum
     
class TestCountWords(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(total_treasure({
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}), 15)

    
if __name__ == '__main__':
    unittest.main()