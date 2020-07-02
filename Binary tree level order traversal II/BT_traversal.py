# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res=[]
        if root ==None:
            return res
        def func(node,lev):
            if len(res)==lev:
                res.append([])
            res[lev].append(node.val)
            
            if node.left:
                func(node.left,lev+1)
            if node.right:
                func(node.right,lev+1)
        func(root,0);
        return res[::-1]
