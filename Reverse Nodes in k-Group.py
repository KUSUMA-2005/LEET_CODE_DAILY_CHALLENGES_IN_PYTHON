'''Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]'''


# METHOD 1
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        curr=head
        for _ in range(k):
            if not curr:return head
            curr=curr.next
        prev=None
        curr=head
        for _ in range(k):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        head.next=self.reverseKGroup(curr, k)
        return prev



#METHOD 2

from collections import deque
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy  
        curr = head
        while curr:
            group_nodes = deque()
            for _ in range(k):
                if curr:
                    group_nodes.append(curr)
                    curr = curr.next
            if len(group_nodes) == k:
                while group_nodes:
                    prev_group_end.next = group_nodes.pop() 
                    prev_group_end = prev_group_end.next  
                prev_group_end.next = curr
            else:
                prev_group_end.next = group_nodes[0] if group_nodes else None
        return dummy.next
