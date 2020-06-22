
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def merge(l1, l2):
    head = point = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            point.next = l1
            l1 = l1.next
        else:
            point.next = l2
            l2 = l1
            l1 = point.next.next
        point = point.next
    if not l1:
        point.next=l2
    else:
        point.next=l1
    return head.next

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """

    # head = point = ListNode(0)
    # q = PriorityQueue()
    # for i in range(len(lists)):
    #     if lists[i]:
    #         q.put((lists[i].val, i))
    # while not q.empty():
    #     val, i = q.get()
    #     point.next = ListNode(val)
    #     point = point.next
    #     lists[i] = lists[i].next
    #     if lists[i]:
    #         q.put((lists[i].val, i))
    # return head.next
    
    
    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = merge(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else None

