# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=head
        slow=head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        prev=None
        while slow: 
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt
        left,right=head,prev
        max_sum=0
        while left and right:
            total=left.val+right.val
            max_sum=max(max_sum,total)
            left=left.next
            right=right.next
        return max_sum

