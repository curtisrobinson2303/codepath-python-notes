"""
Problem 2: Protein Folding Loop Detection
As a biochemist, you're studying the folding patterns of proteins, which are represented as a sequence of amino acids linked together. These proteins sometimes fold back on themselves, creating loops that can impact their function.

Given the head of a linked list protein where each node in the linked list represents an amino acid in the protein, return an array with the values of any cycle in the list. A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.

The values may be returned in any order.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    pass
Example Usage:

Linked list with 4 nodes and a cycle where 4th node points to 2nd node

protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next

print(cycle_length(protein_head))
Example Output:

['Gly', 'Leu', 'Val']
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def cycle_length(protein):
    slow, fast = protein, protein
    res = []
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast.value == slow.value:
            slow = slow.next
            res.append(slow.value)
            while slow.value != fast.value:
                slow = slow.next
                res.append(slow.value)
    return res

    """
    # searching for the cycle
    if not head:
        return False
    
    slow = head  # Starts at the head
    fast = head  # Also starts at the head

    while fast and fast.next:
        slow = slow.next          # Move slow pointer by one
        fast = fast.next.next     # Move fast pointer by two

        if slow == fast:          # If they meet, there's a cycle
            return True
    
    return False  # If fast reaches the end, no cycle
    # ---------------
     """


protein_head = Node("Ala", Node("Gly", Node("Leu", Node("Val"))))
protein_head.next.next.next.next = protein_head.next

print(cycle_length(protein_head))
