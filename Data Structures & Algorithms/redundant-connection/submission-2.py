class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # cycle detection
        graph = {}
        n = len(edges)
        for node in range(1,n+1):
            graph[node] = []    
        visited = set()

        # now we want a DFS that returns TRUE when it finds a cycle
        def dfs(node,parent):
            if node in visited:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor==parent:
                    continue
                if dfs(neighbor,node):
                    return True
            return False

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            visited = set()
            if dfs(a,-1):
                return [a,b]

        return []
            