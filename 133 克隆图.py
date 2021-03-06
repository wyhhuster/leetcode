class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
from collections import deque
class Solution(object):
    #深度优先
    def __init__(self):
        self.visited={}
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        clone_node=Node(node.val,[])
        self.visited[node]=clone_node
        clone_node.neighbors=[self.cloneGraph(n_node) for n_node in node.neighbors]
        return clone_node
    #广度优先

    def cloneGraph1(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        visited = {}
        # 将题目给定的节点添加到队列
        queue = deque([node])
        # 克隆第一个节点并存储到哈希表中
        visited[node] = Node(node.val, [])
        # 广度优先搜索
        while queue:
            # 取出队列的头节点
            n = queue.popleft()
            # 遍历该节点的邻居
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # 如果没有被访问过，就克隆并存储在哈希表中
                    visited[neighbor] = Node(neighbor.val, [])
                    # 将邻居节点加入队列中
                    queue.append(neighbor)
                # 更新当前节点的邻居列表
                visited[n].neighbors.append(visited[neighbor])

        return visited[node]
