class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    #先转为数组 然后构建树
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        li=[]
        while head:
            li.append(head.val)
            head=head.next
        def construct(inorder):
            if len(inorder)==0:
                return None
            if len(inorder)==1:
                return TreeNode(inorder[0])
            index=len(inorder)//2
            mid=inorder[index]
            root=TreeNode(mid)
            root.left=construct(inorder[:index])
            root.right=construct(inorder[index+1:])
            return root
        r=construct(li)
        return r

    #递归
    class Solution:
        def sortedListToBST(self, head):
            ###找到中间节点 断开   去掉中间节点
            ### 左子树等于递归 左边那段   右子树等于递归右边那段
            fast = head
            slow = head
            pre = head
            if not head:
                return
            while (fast and fast.next):
                fast = fast.next.next
                pre = slow
                slow = slow.next
            root = TreeNode(slow.val)
            if slow == fast:
                return root
            pre.next = None
            next_head = slow.next
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(next_head)
            return root