# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        itr=root
        while itr:
            if p.val>itr.val and q.val>itr.val:
                itr=itr.right
            if p.val<itr.val and q.val<itr.val:
                itr=itr.left
            else:
                return itr
        