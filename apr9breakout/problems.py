class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

"""
V1P1

        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3

      Root
      /  
    Node1
    /
  Leaf1  


You have a trailing ivy plant represented by a binary tree. 
You want to take a cutting to start a new plant using the rightmost vine in the plant. Given the root of the plant, return a list with the value of each node in the path from the root node to the rightmost leaf node.
"""


# Problem 1 Iterative right vine approach
# print("Problem 1\n")
def right_vine(root):
  # while node.right child is not none 
  # add the current value to the result list
  # iterate to the next right child 
  #  add to result
  #  return once the right leaf is found
  res = []
  curr = root
  while curr is not None: 
      res.append(curr.val)
      curr = curr.right
  return res

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


# print(right_vine(ivy1))
# print(right_vine(ivy2))



# print("\nProblem 2\n")
# Problem 2 Recursive right vine approach
def right_vine(root):
    # store current valu 
    result = [root.val]
    # if the right node exists recall right vine 

    if root.right is not None: 
        rightVine = right_vine(root.right)
        result = result.extend(rightVine)

    return result

ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))\

# print(right_vine(ivy2))



print("Problem 3")
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    # define the result list with the current root value
    result = []

    # explore the left sub tree and append values to result list
    if root.left is not None: 
        result.extend(survey_tree(root.left))

    # explore the right sub tree and append values to result list
    if root.right is not None: 
        result.extend(survey_tree(root.right))
    # return the result

    result.append(root.val)

    return result

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")), TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3"))) # ['Leaf1', 'Node1', 'Leaf2', 'Leaf3', 'Node2', 'Root']

print(survey_tree(magnolia))

"""
Problem 4: Sum Inventory
A local flower shop stores its inventory in a binary tree, 
where each node represents their current stock of a flower variety. 
Given the root of a binary tree inventory, return the sum of all the flower stock in the store.

Evaluate the time and space complexity of your function. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. 
Assume the input tree is balanced when calculating time and space complexity.
"""

print("\nProblem 4\n")

def sum_inventory(inventory):
    # define the result list with the current root value
    result = int(inventory.val)

    # explore the left sub tree and append values to result list
    if inventory.left is not None: 
        result = result + sum_inventory(inventory.left)

    # explore the right sub tree and append values to result list
    if inventory.right is not None: 
        result = result + sum_inventory(inventory.right)
    # return the result

    return result

    """
     40
    /  \
   5   10
  /   /  \
20   1   30
"""

inventory = TreeNode(40, 
                    TreeNode(5, TreeNode(20)),
                            TreeNode(10, TreeNode(1), TreeNode(30)))

print(sum_inventory(inventory))


"""
Problem 5: Calculating Yield II
You have a fruit tree represented as a binary tree. Given the root of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:

Leaf nodes have an integer value.
Non-leaf nodes have a string value of either "+", "-", "*", or "-".
The yield of a the tree is calculated as follows:

If the node is a leaf node, the yield is the value of the node.
Otherwise evaluate the node's two children and apply the mathematical operation of its value with the children's evaluations.
Return the result of evaluating the root node.

Evaluate the time and space complexity of your function. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.
"""

print("\nProblem 5\n")
def get_decision(root):
    
    # define the result list with the current root value
    result = 0

    # leaf found
    if root.left is None and root.right is None: 
        return root.val
    
    left = get_decision(root.left)
    right = get_decision(root.right) 

    match root.val:
      case "-": 
        result = left - right
      case "+": 
          result = left + right
      case "*": 
          result = left * right
      case _: 
          result = 0 # default case
    
    return result
    
"""

      +
     / \ 
    /   \
   -     *
  / \   / \
 4   2 10  2
"""

root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(get_decision(root))

print("\nProblem 6 \n")

"""
Problem 6: Plant Classifications
Given the root of a binary tree used to classify plants where each level of the tree represents a higher degree of speficity, 
return an array with the most specific plant classification categories (aka the leaf node values). Leaf nodes are nodes with no children.

Evaluate the time and space complexity of your function. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. 
Assume the input tree is balanced when calculating time and space complexity.
"""

def get_most_specific(root):
    # define the result list with the current root value
    result = []

    # explore the left sub tree and append values to result list
    if root.left is None and root.right is None: 
        result.append(root.val)

    if root.left is not None:  
        result.extend(get_most_specific(root.left))

    if root.right is not None: 
        result.extend(get_most_specific(root.right))
      
    return result

"""
           Plantae
          /       \
         /         \
        /           \ 
Non-flowering     Flowering
   /      \       /        \
Mosses   Ferns Gymnosperms Angiosperms
                             /     \
                        Monocots  Dicots
"""
plant_taxonomy = TreeNode("Plantae", 
                          TreeNode("Non-flowering", TreeNode("Mosses"), TreeNode("Ferns")),
                                  TreeNode("Flowering", TreeNode("Gymnosperms"), 
                                          TreeNode("Angiosperms", TreeNode("Monocots"), TreeNode("Dicots"))))

print(get_most_specific(plant_taxonomy))
# ['Mosses', 'Ferns', 'Gymnosperms', 'Monocots', 'Dicots']

print("Problem 7")

"""
Problem 7: Count Old Growth Trees
Given the root of a binary tree where each node represents the age of a tree in a forest, 
write a function count_old_growth() that returns the number of old growth trees in the forest. 
A tree is considered old growth if it has age greater than threshold.

Evaluate the time and space complexity of your function. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. 
Assume the input tree is balanced when calculating time and space complexity.
"""

def count_old_growth(root, threshold):
    result = 0
          
    if root.val > threshold: 
        result += 1

    if root.left is not None: 
        result = result + count_old_growth(root.left, threshold)

    if root.right is not None: 
        result = result + count_old_growth(root.right, threshold)

    return result

"""
     100
     /  \
    /    \
  1200  1500
  /     /  \
20    700  2600
"""

forest = TreeNode(100, TreeNode(1200, TreeNode(20)), TreeNode(1500, TreeNode(700), TreeNode(2600)))

print(count_old_growth(forest, 1000))

print("Problem 8: Twinning Trees")

def is_identical(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False
    
    return root1.val == root2.val and is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right) 


"""
      1                1
     / \              / \
    2   3            2   3  
"""
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))

"""
      1                1
     /                  \
    2                    2  
"""

root3 = TreeNode(1, TreeNode(2))
root4 = TreeNode(1, None, TreeNode(2))

print(is_identical(root1, root2))
print(is_identical(root3, root4))


https://leetcode.com/problems/binary-tree-cameras/description/ 




# Approach 1: Dynamic Programming
# Intuition

# Let's try to cover every node, starting from the top of the tree and working down. Every node considered must be covered by a camera at that node or some neighbor.

# Because cameras only care about local state, we can hope to leverage this fact for an efficient solution. Specifically, when deciding to place a camera at a node, we might have placed cameras to cover some subset of this node, its left child, and its right child already.

# Algorithm

# Let solve(node) be some information about how many cameras it takes to cover the subtree at this node in various states. There are essentially 3 states:

# [State 0] Strict subtree: All the nodes below this node are covered, but not this node.
# [State 1] Normal subtree: All the nodes below and including this node are covered, but there is no camera here.
# [State 2] Placed camera: All the nodes below and including this node are covered, and there is a camera here (which may cover nodes above this node).
# Once we frame the problem in this way, the answer falls out:

# To cover a strict subtree, the children of this node must be in state 1.
# To cover a normal subtree without placing a camera here, the children of this node must be in states 1 or 2, and at least one of those children must be in state 2.
# To cover the subtree when placing a camera here, the children can be in any state.

