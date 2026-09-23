class Solution:
    def isPalindrome(self, s: str) -> bool:
        # using one pointer from the start and oen from the end
        s = s.lower()
        new_str = ""

        for char in s:
            if char.isalnum():
                new_str+=char

        n = len(new_str)
      

        for i in range(0,n//2):
            if new_str[i]!=new_str[n-1-i]:
                    return False
        return True