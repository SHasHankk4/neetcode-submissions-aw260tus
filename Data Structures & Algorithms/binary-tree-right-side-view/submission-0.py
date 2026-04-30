# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_list=[]
        
        def right(root,depth):
            if not root:
                return None
            if depth==len(right_list):
                right_list.append(root.val)
            right(root.right,depth+1)
            right(root.left,depth+1)
            return right_list
        right(root,0)
        return right_list