# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.arr = []
        self.inorder(root)
        l = [self.arr[i] - self.arr[i-1] for i in range(1, len(self.arr))]
        return min(l)
    
    def inorder(self, root: TreeNode) -> int:
        if root.left:
            self.inorder(root.left)
        self.arr.append(root.val)
        if root.right:
            self.inorder(root.right)