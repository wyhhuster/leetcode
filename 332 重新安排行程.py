class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from_to={}
        path={}
        for ticket in tickets:
            if ticket[0] not in from_to:
                from_to[ticket[0]]={}
                path[ticket[0]]=[]
            if ticket[1] not in from_to[ticket[0]]:
                from_to[ticket[0]][ticket[1]]=0
            from_to[ticket[0]][ticket[1]]+=1
            path[ticket[0]].append(ticket[1])
        for key in path.keys():
            path[key]=sorted(path[key])
        res=[]
        flag=0
        def dfs(u):
            nonlocal flag
            res.append(u)
            if len(res) == len(tickets) + 1:
                flag = 1
                return
            if u not in path.keys():
                res.pop()
                return
            for to in path[u]:
                if from_to[u][to] :
                    from_to[u][to]-=1
                    dfs(to)
                    if not flag:
                        from_to[u][to]+=1
            if not flag:
                res.pop()
        dfs('JFK')
        return res
import collections

class Solution1:
    def findItinerary(self, tickets):
        paths = collections.defaultdict(list)
        for start, tar in tickets:
            paths[start].append(tar)
        for start in paths:
            paths[start].sort(reverse=True)
        s = []
        def search(start):
            while paths[start]:
                search(paths[start].pop())
            s.append(start)
        search("JFK")
        return s[::-1]


A=Solution()
print(A.findItinerary( [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))