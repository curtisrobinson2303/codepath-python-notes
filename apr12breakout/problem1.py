from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
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


# def sort_plants(collection):
#     # in order traversal of a BST
#     result = []
#     # base case 
#     if collection.left is None and collection.right is None: 
#         return (collection.key, collection.val)
#     #  explore left sub tree
#     if collection.left is not None: 
#         result += [(sort_plants(collection.left))]
#     #  explore right sub tree
#     if collection.right is not None: 
#         result += [sort_plants(collection.right)]
#     # return the current sub tree
#     return result

def sort_plants(collection): 
    result = []

    if collection.left: 
        result.extend(sort_plants(collection.left))

    result.append((collection.key, collection.val))

    if collection.right: 
        result.extend(sort_plants(collection.right))

    return result


# Using build_tree() function at the top of page
values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)

print(sort_plants(collection))

# expected output: 
# [(1, 'Pothos'), (2, 'Spider Plant'), (3, 'Monstera'), (4, 'Hoya Motoskei'), (5, 'Witchcraft Orchid')]

