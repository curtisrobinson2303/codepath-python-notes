"""
Write a function to find the minimum depth of a binary treee. The minimum depth is the numbr of nodes along the shortest path from the root node down to the nearest leaf node.
Example:
Input: root = [3, 9, 20, null, null, 15, 7]
Output: 2

"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function
def findMinDepth(root):
    # Edge Case Check
    if not root:
        return 0

    # Define global Variables for helper loop
    queue = deque()
    queue.append([root, 1])

    while queue:
        instance = queue.popleft()
        node = instance[0]
        depth = instance[1]

        # checking to see if the current node is a leaf
        if not node.right and not node.left:
            return depth

        if node.left:
            queue.append([node.left, depth + 1])
        if node.right:
            queue.append([node.right, depth + 1])


# Test cases
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(findMinDepth(root))

# Approach:
# I - root of a binary tree
# O - integer value that is the min depth of a binary tree
# C - must find the minimum not just any depth
# E - when depth is 1 or root is null
