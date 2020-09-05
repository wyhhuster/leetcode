"""-------------------------------------------------
 File Name：  60 第k个排列.py
 Author :  wang yuhang
 time：   2020/9/5 11:03
-------------------------------------------------"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return (n * factorial(n - 1))
        def C(m,n):
            return int(factorial(m)/factorial(n)/factorial(m-n))
        def A(m,n):
            return int(factorial(m)/factorial(m-n))
        ans=''
        start=1
        index=0
        visitlist=[]
        for i in range(1,n+1):
            visitlist.append(i)
        while len(ans)<n:
            if k<=A(n-len(ans)-1,n-len(ans)-1):
                ans+=str(start)
                visitlist.remove(start)
                if len(visitlist)==0:
                    break
                start=visitlist[0]
                index=0
            else:
                k-=A(n-len(ans)-1,n-len(ans)-1)
                index+=1
                start=visitlist[index]
        return ans


class Solution1:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)

        k -= 1
        ans = list()
        valid = [1] * (n + 1)
        for i in range(1, n + 1):
            order = k // factorial[n - i] + 1
            for j in range(1, n + 1):
                order -= valid[j]
                if order == 0:
                    ans.append(str(j))
                    valid[j] = 0
                    break
            k %= factorial[n - i]

        return "".join(ans)
# class Solution {
#     public String getPermutation(int n, int k) {
#         int[] factorial = new int[n];
#         factorial[0] = 1;
#         for (int i = 1; i < n; ++i) {
#             factorial[i] = factorial[i - 1] * i;
#         }
# 
#         --k;
#         StringBuffer ans = new StringBuffer();
#         int[] valid = new int[n + 1];
#         Arrays.fill(valid, 1);
#         for (int i = 1; i <= n; ++i) {
#             int order = k / factorial[n - i] + 1;
#             for (int j = 1; j <= n; ++j) {
#                 order -= valid[j];
#                 if (order == 0) {
#                     ans.append(j);
#                     valid[j] = 0;
#                     break;
#                 }
#             }
#             k %= factorial[n - i];
#         }
#         return ans.toString();
#     }
# }


A=Solution()
print(A.getPermutation(3,2))