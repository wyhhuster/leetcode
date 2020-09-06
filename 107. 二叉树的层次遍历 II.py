"""-------------------------------------------------
 File Name：  107. 二叉树的层次遍历 II.py
 Author :  wang yuhang
 time：   2020/9/6 12:27
-------------------------------------------------"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue=[]
        queue.append(root)
        res=[]
        while len(queue)!=0:
            temp=[]
            level_root=[]
            for i in queue:
                temp.append(i.val)
                if i.left:
                    level_root.append(i.left)
                if i.right:
                    level_root.append(i.right)
            queue=level_root
            res.append(temp)
        return res[::-1]
root=TreeNode(3)
root1=TreeNode(9)
root2=TreeNode(20)
root3=TreeNode(15)
root4=TreeNode(7)
root.left=root1
root.right=root2
root2.left=root3
root2.right=root4
A=Solution()
print(A.levelOrderBottom(root))
