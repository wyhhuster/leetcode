class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board or not board[0]:
            return board
        def valid(i,j):
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return False
            return True
        i,j=click[0],click[1]
        if board[i][j]=='M':
            board[i][j]='X'
            return board
        direction=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        visited=[[0]*len(board[0]) for _ in range(len(board))]
        def dfs(i,j):
            if board[i][j]=='E':
                visited[i][j]=1
                for ii,ij in direction:
                    if valid(i+ii,j+ij) and board[i+ii][j+ij]=='M':
                        visited[i][j]+=1
                if visited[i][j]==1:
                    board[i][j]='B'
                else:
                    board[i][j]=str(visited[i][j]-1)
            if board[i][j]=='B':
                for ii,ij in direction:
                    if valid(i+ii,j+ij) and not visited[i+ii][j+ij] and board[i+ii][j+ij]=='E':
                        dfs(i+ii,j+ij)
        dfs(i,j)
        return board
A=Solution()
print(A.updateBoard([['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']],[1,2]))






