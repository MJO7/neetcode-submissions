class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # using sliding window
        left = 0

        count_map = defaultdict(int)    

        length_of_longest_substring_with_repeating_character = 0

        for right in range(len(s)):
            count_map[s[right]]+=1
            frequency_of_most_appearing_character = max(count_map.values())
            windowLength = right-left+1
            while windowLength-frequency_of_most_appearing_character > k:
                count_map[s[left]]-=1
                left+=1
                frequency_of_most_appearing_character = max(count_map.values())
                windowLength = right-left+1
            length_of_longest_substring_with_repeating_character = max(length_of_longest_substring_with_repeating_character, windowLength)
       

        return length_of_longest_substring_with_repeating_character
                