# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.seek(root)
        return self.ans
    def __init__(self):
        self.ans=-99999999
    def seek(self,root):
        if not root:
            return 0
        leftvalue=self.seek(root.left)
        rightvalue=self.seek(root.right)

        value1=root.val
        value2=root.val+leftvalue
        value3=root.val+rightvalue
        value4=root.val+leftvalue+rightvalue

        self.ans=max(self.ans,max(value1,value2,value3,value4))
        return max(value1,value2,value3)