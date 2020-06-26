class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
#保留第一次出现的点
class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        have=set()
        p=head
        while p:
            have.add(p.val)
            if p.next and p.next.val in have:
                q=p.next
                while q and q.val in have:
                    q=q.next
                p.next=q
                p=q
            else:
                p=p.next
        return head
    def view(self,head):
        while head:
            print(head.val)
            head=head.next
#不保留任何重复的点
class Solution1:
    def deleteDuplication(self, pHead):
        # write code here
        ppHead=ListNode(0)
        ppHead.next=pHead
        pre=ppHead
        last=pHead
        while last:
            if last.next and last.val==last.next.val:
                while last.next and last.val==last.next.val:
                    last=last.next
                pre.next=last.next
                last=last.next
            else:
                pre=pre.next
                last=last.next
        return ppHead.next