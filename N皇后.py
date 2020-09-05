"""-------------------------------------------------
 File Name：  N皇后.py
 Author :  wang yuhang
 time：   2020/9/3 12:15
-------------------------------------------------"""
import copy
class Solution(object):
    def __init__(self):
        self.res=[]
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        qipan=[['.']*n for _ in range(n)]
        self.N_queue(qipan,n,0)
        return self.res

    def N_queue(self,qipan,n,num):
        def valid(x,y):
            x1,x2,x3,x4=x,x,x,x
            y1,y2,y3,y4=y,y,y,y
            for i in range(n):
                if qipan[i][y]=='Q':
                    return False
            while x1>=0 and y1>=0:
                if qipan[x1][y1]=='Q':
                    return False
                x1-=1
                y1-=1
            while x2<n and y2<n:
                if qipan[x2][y2]=='Q':
                    return False
                x2+=1
                y2+=1
            while x3>=0 and y3<n:
                if qipan[x3][y3]=='Q':
                    return False
                x3-=1
                y3+=1
            while x4<n and y4>=0:
                if qipan[x4][y4]=='Q':
                    return False
                x4+=1
                y4-=1
            return True
        if num==n:
            a=[]
            for i in qipan:
                a.append(''.join(i))
            self.res.append(a)
            return
        for i in range(n):
            if valid(num,i):
                qipan[num][i]='Q'
                self.N_queue(qipan,n,num+1)
                qipan[num][i]='.'
def helper(positions, row, n):
    if row == n:
        yield ['.' * p + 'Q' + (n-p-1) * '.' for p in positions]
    else:
        for p in range(n):
            if any(p == j or abs(p-j) == row - i for i, j in enumerate(positions)):
                continue
            positions.append(p)
            yield from helper(positions, row+1, n)
            positions.pop()

class Solution1:
    def solveNQueens(self, n):
        return list(helper([], 0, n))
A=Solution()
print(A.solveNQueens(4))

