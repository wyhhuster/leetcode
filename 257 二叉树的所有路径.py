"""-------------------------------------------------
 File Name：  257 二叉树的所有路径.py
 Author :  wang yuhang
 time：   2020/9/4 10:15
-------------------------------------------------"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        self.res=[]
        def find(r,path):
            if not r:
                return
            if not r.left and not r.right:
                path+=[r.val]
                a=list(map(str,path))
                self.res.append('->'.join(a))
                return
            find(r.left,path+[r.val])
            find(r.right,path+[r.val])
        find(root,[])
        return self.res

A=Solution()
root=TreeNode(11)
root2=TreeNode(22)
root3=TreeNode(53)
root4=TreeNode(31)
root.left=root2
root.right=root4
root2.right=root3
print(A.binaryTreePaths(root))
