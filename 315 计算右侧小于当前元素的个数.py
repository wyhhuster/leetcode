class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import bisect
        count=[0]*len(nums)
        sortnums=[]
        for i in range(len(nums)-1,-1,-1):
            position=bisect.bisect_left(sortnums,nums[i])
            count[i]=position
            bisect.insort_left(sortnums,nums[i])
        return count
    def countSmaller1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        indexs=[i for i in range(len(nums))]
        temp=[0 for i in range(len(nums))]
        ans=[0 for i in range(len(nums))]

        self.merge(nums,0,len(nums)-1,indexs,temp,ans)
        return ans,indexs
    def merge(self,nums,low,high,indexs,temp,ans):
        if low<high:
            mid=low+(high-low)//2
            self.merge(nums,low,mid,indexs,temp,ans)
            self.merge(nums,mid+1,high,indexs,temp,ans)
            self.count(nums,low,mid,high,indexs,temp,ans)
    def count(self,nums,low,mid,high,indexs,temp,ans):
        for i in range(low,high+1):
            temp[i]=indexs[i]
        l=low
        h=mid+1
        k=low
        while l<=mid and h<=high:
            if nums[temp[l]]<=nums[temp[h]]:
                indexs[k]=temp[l]
                l+=1
                ans[indexs[k]]+=h-mid-1
                k+=1
            else:
                indexs[k]=temp[h]
                h+=1
                k+=1
        while l<=mid:
            indexs[k]=temp[l]
            l+=1
            ans[indexs[k]]+=high-mid
            k+=1
        while h<=high:
            indexs[k]=temp[h]
            h+=1
            k+=1
A=Solution()
print(A.countSmaller1([5,2,6,1]))