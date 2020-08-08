class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#中序遍历得到结果后再寻找
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        node1,node2=None,None
        for i in range(len(self.order)-1):
            if self.order[i].val>self.order[i+1].val and node1==None:
                node1=self.order[i]
                node2=self.order[i+1]
            elif self.order[i].val>self.order[i+1].val and node1!=None:
                node2=self.order[i+1]
        node1.val, node2.val = node2.val, node1.val
    def __init__(self):
        self.order=[]
    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        self.order.append(root)
        self.inorder(root.right)
#在中序遍历的过程中确定
class Solution2(object):
    #非递归
    def inorder1(self,root):
        stack=[]
        x,y,pred=None,None,None
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            p=stack.pop()
            if pred and p.val <pred.val:
                y=p
                if not x:
                    x=pred
                else:
                    break
            pred=p
            root=p.right
        x.val,y.val=y.val,x.val
    #递归
    def __init__(self):
        self.x,self.y,self.pre=None,None,None
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        self.x.val,self.y.val=self.y.val,self.x.val

    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        if self.pre and root.val<self.pre.val:
            self.y=root
            if not self.x:
                self.x=self.pre
        self.pre=root
        self.inorder(root.right)






