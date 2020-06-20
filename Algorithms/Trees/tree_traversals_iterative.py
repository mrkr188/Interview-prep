# Iterative tree traversals 

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


# inorder tree traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31313/three-ways-of-iterative-inorder-traversing-easy-explanation
def inorder_traversal_iterative(root):
    # check for empty tree
    if root is None: 
        return []
    stack = []
    res = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            res.append(node.val)
            root = node.right
    return res

# preorder tree traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/45312/three-ways-of-iterative-preorder-traversing-easy-explanation
def preorder_traversal_iterative(root): 
    # check for empty tree
    if root is None: 
        return []
    res = []
    stack = []
    while root or stack:
        if root:
            res.append(root.val)
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            root = root.right
    return res


# postorder tree traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45648/three-ways-of-iterative-postorder-traversing-easy-explanation
def postorder_traversal_iterative(root): 
    # check for empty tree
    if root is None: 
        return []
    res = []
    stack = []
    pre = None
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack[-1]
            if root.right == None or root.right == pre:
                res.append(root.val)
                stack.pop()
                pre = root
                root = None
            else:
                root = root.right
    return res


# Driver
root = Node(1) 
root.left	 = Node(2) 
root.right	 = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 


print("Inorder traversal of binary tree is")
print(inorder_traversal_iterative(root))


print("Preorder traversal of binary tree is")
print(preorder_traversal_iterative(root))


print("Postorder traversal of binary tree is")
print(postorder_traversal_iterative(root))