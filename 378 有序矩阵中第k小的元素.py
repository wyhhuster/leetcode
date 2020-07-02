import heapq
import List
class Solution(object):
    #最小堆 从每一行开始寻找
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n=len(matrix)
        pq=[(matrix[i][0],i,0) for i in range(n)]
        heapq.heapify(pq)
        for i in range(k-1):
            num,i,j=heapq.heappop(pq)
            if j!=n-1:
                heapq.heappush(pq,(matrix[i][j+1],i,j+1))
        return heapq.heappop(pq)[0]
    #二分
    #https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/you-xu-ju-zhen-zhong-di-kxiao-de-yuan-su-by-leetco/
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
















