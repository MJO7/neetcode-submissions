class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # word ladder
        # goooood anakin....gooood.
        if endWord not in wordList:
            return 0
        neighbors = collections.defaultdict(list)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbors[pattern].append(word)

        queue = deque()
        queue.append(beginWord)
        visited = set()
        visited.add(beginWord)
        length = 1
        while queue:
            for i in range(len(queue)):
                popped_word = queue.popleft()
                if popped_word==endWord:
                    return length

                for j in range(len(popped_word)):
                    pattern = popped_word[:j] + "*" + popped_word[j+1:]
                    for neighbor_word in neighbors[pattern]:
                        if (neighbor_word not in visited):
                            queue.append(neighbor_word)
                            visited.add(neighbor_word)  
            length+=1
        return 0