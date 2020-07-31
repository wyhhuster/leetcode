# 魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。
# 给定一个有序整数数组，编写一种方法找出魔术索引，
# 若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。
class Solution(object):
    #遍历
    def findMagicIndex1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag=0
        for i in range(len(nums)):
            if nums[i]==i:
                flag=1
                break
        if flag:
            return i
        else:
            return -1

    #分治
    def findMagicIndex2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find(nums,left,right):
            if left>right:
                return -1
            mid=left+(right-left)//2
            leftans=find(nums,left,mid-1)
            if leftans!=-1:
                return leftans
            elif nums[mid]==mid:
                return mid
            return find(nums,mid+1,right)

        ans=find(nums,0,len(nums)-1)
        return ans

    def findMagicIndex3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right=0,len(nums)-1
        while left<=right:
            if nums[left]==left:
                return left
            elif nums[left]>left:
                left=nums[left]
            else:
                left+=1
        return -1
