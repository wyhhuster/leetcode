class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board
        self.change=[]
        visited=[[False]*len(board[0]) for _ in range(len(board))]
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        def valid(i,j):
            if i<len(board)-1 and 0<i and j>0 and j<len(board[0])-1:
                return True
            return False
        def extend(i,j):
            for ii,ij in direction:
                if valid(i+ii,j+ij) and not visited[i+ii][j+ij] and board[i+ii][j+ij]=='O':
                    print(i+ii,j+ij)
                    visited[i+ii][j+ij]=True
                    self.change.append([i+ii,j+ij])
                    extend(i+ii,j+ij)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i==0 or j==0 or i==len(board)-1 or j==len(board[0])-1:
                    if board[i][j]=='O':
                        extend(i,j)
        for i in range(1,len(board)-1):
            for j in range(1,len(board[0])-1):
                if board[i][j]=='O' and [i,j] not in self.change:
                    board[i][j]='X'
        return board



A=Solution()
print(A.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
