# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverFromPreorder(self, s):
        """
        :type S: str
        :rtype: TreeNode
        """
        dic={-1:TreeNode(0)}
        dep=0
        value=''
        for i in range(len(s)):
            if s[i]!='-':
                value+=s[i]
            elif value:
                dic[dep]=TreeNode(int(value))
                if not dic[dep-1].left:
                    dic[dep-1].left=dic[dep]
                else:
                    dic[dep-1].right=dic[dep]
                value=''
                dep=1
            else:
                dep+=1
        dic[dep]=TreeNode(int(value))
        if not dic[dep-1].left:
            dic[dep-1].left=dic[dep]
        else:
            dic[dep-1].right=dic[dep]
        return dic[0]