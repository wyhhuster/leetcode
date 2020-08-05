class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def seek(root):
            if not root:
                return [0, 0]
            left = seek(root.left)
            right = seek(root.right)
            rootsteal = root.val + left[1] + right[1]
            rootnonsteal = max(left[0], left[1]) + max(right[0], right[1])
            return [rootsteal, rootnonsteal]

        result = seek(root)
        return max(result)