class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        mid=len(nums)//2
        root=TreeNode(nums[mid])
        root.left=self.sortedArrayToBST(nums[:mid])
        root.right=self.sortedArrayToBST(nums[mid+1:])
        return root
    def view(self,root):
        if root:
            print(root.val)
            self.view(root.left)
            self.view(root.right)
A=Solution()

r=A.sortedArrayToBST([-10,-3,0,5,9])
A.view(A.sortedArrayToBST([-10,-3,0,5,9]))