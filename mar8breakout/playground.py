import unittest


def score_of_mystical_market_chains(chain):
    """
    I - String of parentheses as input
    O - a int score
    C - Constraints need stack to deal with nested parentheses
    E - length is 0 or 1 count == 0

    Plan:
        Key Ideas:
            - Must use the stack to keep track of the open parens
        Steps:
            1. define stack, and count variable
            2. iterate through string char by char
                - if char is "(" push to stack
                - else pop item from stack and compare to open paren to see if balanced
                    - if valid pair: add 1 to the count
                    - edge case: must ensure the stack has at least 1 item on it
                - repeat
    """

    stack = []
    count = 0

    for char in chain:
        if char == "(":
            stack.append(char)
        elif char == ")" and len(stack) > 0:
            if char == ")" and stack.pop() == "(":
                count += 1
        else:
            continue

    return count


class TestProcessData(unittest.TestCase):
    def test_example_1(self):
        # Example test case (replace with your specific tests)
        self.assertEqual(score_of_mystical_market_chains("()"), 1)

    def test_example_2(self):
        # Example test case (replace with your specific tests)
        self.assertEqual(score_of_mystical_market_chains("(())"), 2)

    def test_example_3(self):
        # Example test case (replace with your specific tests)
        self.assertEqual(score_of_mystical_market_chains("()()"), 2)


if __name__ == "__main__":
    unittest.main()
