# Recursive tree traversals 


# Example tree
#            1
#           / \
#          2   3
#         / \
#        4   5

# Depth First Traversals:
# (a) Inorder (Left, Root, Right) : 4 2 5 1 3
# (b) Preorder (Root, Left, Right) : 1 2 4 5 3
# (c) Postorder (Left, Right, Root) : 4 5 2 3 1

# Breadth First or Level Order Traversal : 1 2 3 4 5


# class that represents an individual node in a binary tree 
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 


# function to do inorder tree traversal 
def inorder_traversal(root): 
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []



# function to do postorder tree traversal 
def postorder_traversal(root): 
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val] if root else []


# function to do preorder tree traversal 
def preorder_traversal(root): 
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []


def level_order_traversal(root):
    if not root:
        return []
    queue = [root]
    res = []
    while queue:
        res.extend([node.val for node in queue])
        queue = [child for i in queue for child in (i.left, i.right) if child]
    return res


# Driver code 
root = Node(1) 
root.left	 = Node(2) 
root.right	 = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 


print("Preorder traversal of binary tree is")
print(inorder_traversal(root))

print("\nInorder traversal of binary tree is")
print(postorder_traversal(root))

print("\nPostorder traversal of binary tree is")
print(preorder_traversal(root))

print("\nLevelorder traversal of binary tree is")
print(level_order_traversal(root))

