
class Solution:
    def PredictTheWinner(self, nums):
        length = len(nums)
        dp = [[0] * length for _ in range(length)]
        for i, num in enumerate(nums):
            dp[i][i] = num
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                print(i,j)
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][length - 1] >= 0
class Solution2:
    def PredictTheWinner(self, nums):
        length = len(nums)
        dp = [0] * length
        for i, num in enumerate(nums):
            dp[i] = num
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[length - 1] >= 0
# class Solution {
#     public boolean PredictTheWinner(int[] nums) {
#         int length = nums.length;
#         int[][] dp = new int[length][length];
#         for (int i = 0; i < length; i++) {
#             dp[i][i] = nums[i];
#         }
#         for (int i = length - 2; i >= 0; i--) {
#             for (int j = i + 1; j < length; j++) {
#                 dp[i][j] = Math.max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
#             }
#         }
#         return dp[0][length - 1] >= 0;
#     }
# }

A=Solution()
print(A.PredictTheWinner([1, 5, 233, 7]))