# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
r1=TreeNode(1)
r2=TreeNode(2)
r3=TreeNode(3)
r4=TreeNode(4)
r5=TreeNode(5)
r6=TreeNode(6)
r1.left=r2
r2.left=r3
r2.right=r4
r1.right=r5
r5.right=r6
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        stack=[]
        p=root
        preorder=[]
        while p or stack:
            if p:
                stack.append(p)
                preorder.append(p)
                p=p.left
            else:
                p=stack.pop()
                p=p.right
        head=preorder[0]
        p=head
        for inedx,node in enumerate(preorder[1:]):
            p.right=node
            p.left=None
            p=p.right
        return head
A=Solution()
print(A.flatten(r1))

