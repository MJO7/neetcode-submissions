class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited =set()
        def dfs(node,parent):            
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor==parent:
                    continue
                elif neighbor not in visited:
                    dfs(neighbor,node)
        
        res = 0

        for node in range(n):
            if (node not in visited):
                res+=1
                dfs(node,-1)

        return res
