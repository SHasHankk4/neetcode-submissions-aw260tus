# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) :
        q=deque()
        if root:
            q.append(root)
        
        counter=0
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            counter+=1
        return counter
        