# https://leetcode.com/problems/copy-list-with-random-pointer/

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        # 1st pass - add new nodes adjacent to old nodes
        curr = head
        while curr:
            new_node = Node(curr.val, None, None)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
            
        # 2nd pass - update random nodes 
        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        
        # 3rd pass - remove connections
        old_list = head # A->B->C
        new_list = head.next # A'->B'->C'
        new_head = head.next
        while new_list.next:
            old_list.next = old_list.next.next
            new_list.next = new_list.next.next
            old_list = old_list.next
            new_list = new_list.next
        return new_head
    



        