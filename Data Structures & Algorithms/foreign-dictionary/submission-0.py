class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # first we have to make an adjacency list
        adjacencyList = {}
        for word in words:
            for char in word:
                if char not in adjacencyList:
                    adjacencyList[char] = set()
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjacencyList[w1[j]].add(w2[j])
                    break
        
        # now cycle detection using Post order DFS
        visit = set()
        current = set()
        res = []

        def dfs(c):
            if c in current:
                return True
            if c in visit:
                return False
            
            current.add(c)

            for neighbor in adjacencyList[c]:
                if dfs(neighbor):
                    return True
            
            current.remove(c)
            visit.add(c)        
            res.append(c)
        
        for c in adjacencyList:
            if dfs(c):
                return ""
        
        return "".join(res[::-1])