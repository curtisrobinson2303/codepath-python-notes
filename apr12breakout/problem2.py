class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right


def find_flower(inventory, name):
    if inventory.val == name: 
        return True
    if inventory.left: 
        if find_flower(inventory.left, name): 
            return True
    if inventory.right: 
        if find_flower(inventory.right, name): 
            return True
    return False

"""
         Rose
        /    \
      Lily   Tulip
     /  \       \
  Daisy  Lilac  Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 

#  Example Output:
# True
# False