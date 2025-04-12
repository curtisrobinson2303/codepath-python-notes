class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def remove_plant(collection, name):
    #  if the current node is a leaf we just delete it
    #  if the current node is a parent of a leaf we must take the left child and make that the new parent   
        # assuming that we have a right child
    


    # Approach: 
    #  check root if none return None
    if collection is None:
        return None

    # search through tree to find target node 

    # if name < root.val: 
        # call on left
    if name.val < collection.val:
         
         collection.left = remove_plant(collection.left, name) 
    #  if name > root.val: 
        #  call on right
    if name.val > collection.val:
        collection.right = remove_plant(collection.right, name)
    else:
        if collection.right and collection.left:
        
        if collec
    # else: 
        # check if the root has two chlidren

        #  check if the root has 1 child
        if collection.left is None: 
            return collection.right
        
        if collection.right is None: 
            return collection.left

        #  check if the node is a leaf

    # return root



# Using build_tree() function at the top of page
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(remove_plant(collection, "Pilea"))


['Money Tree', 'Hoya', 'Orchid', None, 'Ivy', None, 'ZZ Plant']


'''
Explanation:
The resulting tree structure:
             Money Tree
            /         \
          Hoya       Orchid
              \          \
              Ivy      ZZ Plant
'''