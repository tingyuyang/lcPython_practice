# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None): # similar as "if root is None".
            return 0
        leftMax = self.maxDepth(root.left) #understand this "self"
        rightMax = self.maxDepth(root.right)
        return max(leftMax,rightMax)+1     #"+1" is for root
