class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited=[0]*len(rooms)
        flag=False
        def dfs(u):
            print(u)
            nonlocal flag
            visited[u]=1
            if visited==[1]*len(rooms):
                flag=True
                return
            for i in rooms[u]:
                if not visited[i]:
                    dfs(i)
            # if not flag:
            #     visited[u]=0
        dfs(0)
        return flag

# class Solution {
#     public boolean canVisitAllRooms(List<List<Integer>> rooms) {
#         boolean[] enter = new boolean[rooms.size()];
#         dfs(rooms, 0, enter);
#         for (boolean flag : enter) {
#             if (!flag) return false;
#         }
#         return true;
#     }
#
#     public void dfs(List<List<Integer>> rooms, int idx, boolean[] enter) {
#         enter[idx] = true;
#         for (int i : rooms.get(idx)) {
#             if (enter[i]) continue;
#             dfs(rooms, i, enter);
#         }
#     }
# }
# class Solution {
#
#     // 841. 钥匙和房间
#     public boolean canVisitAllRooms(List<List<Integer>> rooms) {
#         Set<Integer> set = new HashSet<>();
#         dfs(rooms, 0, set);
#         return set.size() == rooms.size();
#     }
#
#     private void dfs(List<List<Integer>> rooms, int cur, Set<Integer> visited) {
#         if (visited.contains(cur)) return;
#         visited.add(cur);
#         for (Integer next : rooms.get(cur)) {
#             dfs(rooms, next, visited);
#         }
#     }
# }
A=Solution()
print(A.canVisitAllRooms([[2,3],[],[2],[1,3,1]]))