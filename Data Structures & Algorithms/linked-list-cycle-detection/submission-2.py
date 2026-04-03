# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        setval=set()

        while head:
            if head in setval:
                return True
            setval.add(head)
            head=head.next
        return False
