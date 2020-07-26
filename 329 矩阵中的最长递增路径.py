class Solution(object):
    #朴素的深度优先搜索 超时
    def __init__(self):
        self.ans=1
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix)==0:
            return 0
        visited=[[1]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in  range(len(matrix[0])):
                self.findone(matrix,i,j,1,visited)
        return self.ans
    def findone(self,matrix,i,j,length,visited):
        """
        :type matrix: List[List[int]]
        :type visited: List[List[int]]
        """
        visited[i][j]=0
        if i+1<len(matrix) and visited[i+1][j] and matrix[i+1][j]>matrix[i][j]:
            self.ans=max(self.ans,length+1)
            self.findone(matrix,i+1,j,length+1,visited)
        if j+1<len(matrix[0]) and visited[i][j+1] and matrix[i][j+1]>matrix[i][j]:
            self.ans=max(self.ans,length+1)
            self.findone(matrix,i,j+1,length+1,visited)
        if i-1>=0 and visited[i-1][j] and matrix[i-1][j]>matrix[i][j]:
            self.ans=max(self.ans,length+1)
            self.findone(matrix,i-1,j,length+1,visited)
        if j-1>=0 and visited[i][j-1] and matrix[i][j-1]>matrix[i][j]:
            self.ans=max(self.ans,length+1)
            self.findone(matrix,i,j-1,length+1,visited)
        visited[i][j]=1
    #动态规划
    def longestIncreasingPath1(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        lst = []
        for i in range(m):
            for j in range(n):
                lst.append((matrix[i][j], i, j))
        lst.sort()
        print(lst)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for num, i, j in lst:
            dp[i][j] = 1
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r, c = i + di, j + dj
                if 0 <= r < m and 0 <= c < n:
                    if matrix[i][j] > matrix[r][c]:
                        dp[i][j] = max(dp[i][j], 1 + dp[r][c])
        return max([dp[i][j] for i in range(m) for j in range(n)])
    #优化后的深度优先，计算过的点直接返回
    def longestIncreasingPath2(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m=len(matrix)
        n=len(matrix[0])
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        def valid(x,y):
            if x<0 or x>=m or y<0 or y>=n:
                return False
            else:
                return True
        memo=[[0]*n for _ in range(m)]
        def find(matrix,i,j):
            if memo[i][j]!=0:
                return memo[i][j]
            memo[i][j]=1
            for ix,iy in direction:
                if valid(i+ix,j+iy) and matrix[i+ix][j+iy]>matrix[i][j]:
                    memo[i][j]=max(memo[i][j],find(matrix,i+ix,j+iy)+1)
            return memo[i][j]
        ans=0
        for i in range(m):
            for j in range(n):
                ans=max(ans,find(matrix,i,j))
        return ans

