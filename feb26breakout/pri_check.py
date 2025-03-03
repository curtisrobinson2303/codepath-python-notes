import unittest

def can_trust_message(message):
    """
            I - string message 
            O - bool saying if t
            C
            E

            Plan: 
                Key Ideas:
                Steps: 
                    Define a set 

                    iterate through the message adding all valid letters to the set

                    Check length of set 

                    return true if set length  == 26 else false 
            
    """
    another_set = set(message)

    another_set.discard(" ")
    
    if len(another_set) == 26: 
        return True
    else: 
        return False
    
     
class TestCountWords(unittest.TestCase):
    def test_message_1(self):
        self.assertEqual(can_trust_message("sphinx of black quartz judge my vow"), True)
    def test_message_2(self):
        self.assertEqual(can_trust_message("trust me"), False)


    
if __name__ == '__main__':
    unittest.main()