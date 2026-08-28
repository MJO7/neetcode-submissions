class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #the sorted form of all anagrams is the same.
        my_dict = {}
        for i in strs:
            sorted_list = list(i)
            sorted_list.sort()
            sorted_list = tuple(sorted_list)
            if sorted_list not in my_dict:
                my_dict[sorted_list] = [i]
            else:
                my_dict[sorted_list].append(i)
            
        return list(my_dict.values())