#https://leetcode-cn.com/problems/remove-boxes/solution/yi-chu-he-zi-by-leetcode-solution/
class Solution:
    def removeBoxes(self, boxes):
        n = len(boxes)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]
        def helper(i, j, k):
            if i > j:
                return 0
            if dp[i][j][k] != 0:
                return dp[i][j][k]
            # 大段连续的部分肯定是放一起消失得分高，而不是单个消失
            while i < j and boxes[i] == boxes[i + 1]:
                i += 1
                k += 1
            res = (k + 1) ** 2 + helper(i + 1, j, 0)
            for m in range(i + 1, j + 1):
                if boxes[m] == boxes[i]:
                    res = max(res, helper(i + 1, m - 1, 0) + helper(m, j, 1 + k))
            dp[i][j][k] = res
            return dp[i][j][k]
        return helper(0, n - 1, 0)

