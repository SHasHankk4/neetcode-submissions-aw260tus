# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        setval=set()

        while head:
            if head.next.val in setval:
                return True
            else:
                setval.add(head.val)
            head=head.next
        return False
        