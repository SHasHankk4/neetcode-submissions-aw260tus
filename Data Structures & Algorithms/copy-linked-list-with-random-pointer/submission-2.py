"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        HashMap={}
        curr=head
        while curr:
            new_node=Node(curr.val)
            HashMap[curr]=new_node
            curr=curr.next
        curr=head
        while curr:
            new_node=HashMap[curr]
            new_node.next=HashMap[curr.next] if curr.next else None
            new_node.random=HashMap[curr.random] if curr.random else None
            curr=curr.next
        return HashMap[head]
