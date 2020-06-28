class Solution(object):
    def minSubArrayLen1(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        curnum=0
        curarray=[]
        k=0
        start=0
        curlength=0
        ans=999999
        while start<len(nums):
            if curnum<s:
                curnum+=nums[start]
                curarray.append(nums[start])
                start+=1
                curlength+=1
            else:
                while curnum>=s:
                    ans = min(ans, curlength)
                    curnum-=curarray[k]
                    k+=1
                    curlength-=1
        while curnum >= s:
            ans = min(ans, curlength)
            curnum -= curarray[k]
            k += 1
            curlength -= 1

        if ans==999999:
            return 0
        else:
            return ans
    def minSubArrayLen2(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        right,left,ans,cursum=0,0,len(nums)+1,0
        while right<len(nums):
            while cursum<s and right<len(nums):
                cursum+=nums[right]
                right+=1
            while cursum>=s :
                ans=min(ans,right-left)
                cursum-=nums[left]
                left+=1
        return ans

A=Solution()
print(A.minSubArrayLen1(7, [2,3,1,2,4,3]))



