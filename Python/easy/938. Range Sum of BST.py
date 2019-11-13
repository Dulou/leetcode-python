# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res = 0
        if not root:
            return 0
        if L <= root.val and R >= root.val:
            res += root.val
            res += self.rangeSumBST(root.right, L, R)
            res += self.rangeSumBST(root.left, L, R)
        if L > root.val:
            res += self.rangeSumBST(root.right, L, R)
        if R < root.val:
            res += self.rangeSumBST(root.left, L, R)
            

        return res
        