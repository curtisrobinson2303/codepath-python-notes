
from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def add_plant(collection, name):
    # adding plants in by alphabetical order
    # must check to make sure of the ascii values 
    # edge case: when a same letter is found add it to the right
    # if there is no node set the root to be  name

    if collection is None: 
        return TreeNode(name)
    
    if name < collection.val: 
        collection.left = add_plant(collection.left, name)

    else: # changed to else becuase this account for the edge case where the letters are the same and defaults to right insertion
        collection.right = add_plant(collection.right, name)
    
    return collection

"""
            Money Tree
        /              
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))


'''
['Money Tree', 'Fiddle Leaf Fig', 'Snake Plant', 'Aloe']

Explanation: 
Tree should have the following structure:
           Money Tree
        /              \
 Fiddle Leaf Fig   Snake Plant
   /
 Aloe
'''