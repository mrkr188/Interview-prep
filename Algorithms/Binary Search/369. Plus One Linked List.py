# Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

# You may assume the integer do not contain any leading zero, except the number 0 itself.

# The digits are stored such that the most significant digit is at the head of the list.

# Example :

# Input: [1,2,3]
# Output: [1,2,4]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = []
        head = self
        while head:
            res.append(head.val)
            head =  head.next
        return str(res)


def plusOne(head):
    dummy = ListNode(0)
    dummy.next = head
    not_nine = dummy
    
    while head:
        if head.val != 9:
            not_nine = head
        head = head.next
    
    not_nine.val += 1
    not_nine = not_nine.next
    
    while not_nine:
        not_nine.val = 0
        not_nine = not_nine.next
    
    return dummy if dummy.val else dummy.next

head = ListNode(1, ListNode(2, ListNode(3)))
print(plusOne(head))

head = ListNode(9, ListNode(9, ListNode(9)))
print(plusOne(head))

head = ListNode(1, ListNode(9, ListNode(9)))
print(plusOne(head))