class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color=[0]*len(graph)
        Uncolor,Red,Green=0,1,2
        def dfs(node,c):
            color[node] = c
            print(color)
            cNei = (Green if c == Red else Red)
            for neighbor in graph[node]:
                if color[neighbor] == Uncolor:
                    if not dfs(neighbor, cNei):
                        return False
                elif color[neighbor] != cNei:
                    return False
            return True

        for i in range(len(graph)):
            if color[i]==Uncolor:
                if not dfs(i,Red):
                    return False
        return True
A=Solution()
print(A.isBipartite([[3,4,6],[3,6],[3,6],[0,1,2,5],[0,7,8],[3],[0,1,2,7],[4,6],[4],[]]))


class Solution1:
    def isBipartite(self, graph):
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n
        valid = True

        def dfs(node: int, c: int):
            nonlocal valid
            color[node] = c
            print(color)
            cNei = (GREEN if c == RED else RED)
            for neighbor in graph[node]:
                if color[neighbor] == UNCOLORED:
                    dfs(neighbor, cNei)
                    if not valid:
                        return
                elif color[neighbor] != cNei:
                    valid = False
                    return

        for i in range(n):
            if color[i] == UNCOLORED:
                dfs(i, RED)
                if not valid:
                    break

        return valid
A=Solution1()
print(A.isBipartite( [[3,4,6],[3,6],[3,6],[0,1,2,5],[0,7,8],[3],[0,1,2,7],[4,6],[4],[]]))

