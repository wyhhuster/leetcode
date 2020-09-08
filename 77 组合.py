"""-------------------------------------------------
 File Name：  77 组合.py
 Author :  wang yuhang
 time：   2020/9/8 9:35
-------------------------------------------------"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res=[]
        def dfs(num,path,start,end):
            if num==k:
                self.res.append(path[:])
                return
            for i in range(start,end+1):
                path.append(i)
                dfs(num+1,path,i+1,end)
                path.pop()
        dfs(0,[],1,n)
        return self.res
A=Solution()
print(A.combine(4,2))