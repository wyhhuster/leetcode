class Solution(object):
    #二分法
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        left=max(nums)
        right=sum(nums)

        while left<right:
            mid=(left+right)//2
            total,cnt=0,1
            for i in nums:
                if total+i>mid:
                    total=i
                    cnt+=1
                else:
                    total+=i
            if cnt<=m:
                right=mid
            else:
                left=mid+1
        return left
    #动态规划
    def splitArray1(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        f = [[10 ** 18] * (m + 1) for _ in range(n + 1)]
        sub = [0]
        for elem in nums:
            sub.append(sub[-1] + elem)

        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(j-1,i):
                    f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))
        return f[n][m]
A=Solution()
print(A.splitArray1(nums = [7,2,5,10,8],m = 2))

