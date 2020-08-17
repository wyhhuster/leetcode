# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def find(root):
            if not root:
                return 0
            left=find(root.left)
            right=find(root.right)
            if left>=0 and right>=0 and abs(left-right)<=1:
                return max(left,right)+1
            else:
                return -1
        if not root:
            return True
        return find(root)!=-1


