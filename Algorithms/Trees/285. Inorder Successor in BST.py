# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderSuccessor(root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':  
    # if there is right go right for successer
    if p.right:
        node = p.right
        while node.left:
            node = node.left
        return node
    # else go left to find successor
    stack = []
    while stack or root:
        if root:
            if root == p:
                return stack.pop() if stack else None
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            root = node.right
    return None


def inorderSuccessor_(root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    candidate = None  
    while root:
        if root.val <= p.val:
            root = root.right
        elif root.val > p.val:
            candidate = root
            root = root.left
        
    return candidate


# Driver 1
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(inorderSuccessor(root, root.left).val)
print(inorderSuccessor_(root, root.left).val)

# Driver 2
root = TreeNode(5)
root.right = TreeNode(6)
root.left = TreeNode(3)

root.left.right = TreeNode(4)
root.left.left = TreeNode(2)

root.left.left.left = TreeNode(1)

print(inorderSuccessor(root, root.left).val)
print(inorderSuccessor_(root, root.left).val)

# returns None
print(inorderSuccessor(root, root.right))
print(inorderSuccessor_(root, root.right))

# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

# The successor of a node p is the node with the smallest key greater than p.val.

# Example 1:
#      2
#     / \
#    1   3
# Input: root = [2,1,3], p = 1
# Output: 2
# Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

# Example 2:
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1

# Input: root = [5,3,6,2,4,null,null,1], p = 6
# Output: null
# Explanation: There is no in-order successor of the current node, so the answer is null.