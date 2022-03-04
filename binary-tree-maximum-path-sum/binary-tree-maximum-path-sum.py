# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_ = -100000
    def recurr(self, root):
        if root.left == None and root.right == None:
            if self.max_ < root.val:
                self.max_ = root.val
            return root.val
        
        left = 0
        right = 0
        if root.left != None:
            left = self.recurr(root.left)
            if self.max_ < left:
                self.max_ = left
            if self.max_ < left+root.val:
                self.max_ = left+root.val
        if root.right != None:
            right = self.recurr(root.right)
            if self.max_ < right:
                self.max_ = right
            if self.max_ < right+root.val:
                self.max_ = right+root.val
        
        if self.max_ < left + right + root.val:
            self.max_ = left + right + root.val
        if self.max_ < root.val:
            self.max_ = root.val
        
        return max(left+root.val, right + root.val, root.val)
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.recurr(root)
        
        return self.max_
        