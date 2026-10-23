class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {}
        rank = {}
        def find(x):
            if x not in parent:
                parent[x] = x
                rank[x]=0
            while parent[x]!=x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a,b):
            root_a = find(a)
            root_b = find(b)
            if root_a==root_b:
                return False
            if rank[root_a]>rank[root_b]:
                parent[root_b] = root_a
            elif rank[root_a]<rank[root_b]:
                parent[root_a] = root_b
            else:
                parent[root_b] = root_a
                rank[root_a]+=1
            return True

        for a,b in edges:
            if not union(a,b):
                return ([a,b])