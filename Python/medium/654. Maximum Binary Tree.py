# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        maxNum = nums[0]
        index = 0
        length = len(nums)
        
        for i in range(length):
            if nums[i] > maxNum:
                maxNum = nums[i]
                index = i
        
        root = TreeNode(maxNum)
        root.left = self.constructMaximumBinaryTree(nums[:index])
        if index < length - 1:
            root.right = self.constructMaximumBinaryTree(nums[index+1:])
        return root
        