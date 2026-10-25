class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            char_array = [0]*26
            for char in s:
                alphabetical_index = (ord(char) - ord('a'))
                char_array[alphabetical_index] += 1
            res[tuple(char_array)].append(s)
        return list(res.values())