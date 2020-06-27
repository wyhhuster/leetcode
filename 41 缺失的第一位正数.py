from typing import List


class Solution1:

    # 3 应该放在索引为 2 的地方
    # 4 应该放在索引为 3 的地方

    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                self.__swap(nums, i, nums[i] - 1)

        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1

        return size + 1

    def __swap(self, nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]

class Solution2:
    def firstMissingPositive(self, a: List[int]) -> int:
        if len(a)==0:
            return 1
        hash=0
        for i in range(len(a)):
            if a[i]>0 and a[i]<=len(a):
                hash|=1<<a[i]
        ans=0
        for i in range(1,len(a)+2):
            if hash & 1<<i ==0:
                ans=i
                break
        if hash==0:
            return 1
        if ans==0:
            return max(a)+1
        return ans
