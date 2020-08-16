from _collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        target=image[sr][sc]
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        visited=[[0]*len(image[0]) for _ in range(len(image))]
        def valid(i,j):
            if i<0 or i>=len(image) or j<0 or j>=len(image[0]):
                return False
            return True
        change=deque()
        change.append([sr,sc])
        while change:
            sr,sc=change.popleft()
            visited[sr][sc]=1
            image[sr][sc]=newColor
            for isr,isc in direction:
                if valid(sr+isr,sc+isc) and not visited[sr+isr][sc+isc] and image[sr+isr][sc+isc]==target:
                    change.append([sr+isr,sc+isc])
        return image
A=Solution()
print(A.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]],sr = 1, sc = 1, newColor = 2))



