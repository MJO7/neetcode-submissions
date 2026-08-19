class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m+n-1
        j = n-1
        while j>=0:
            nums1_index = i-j-1
            if (nums1_index>=0) and nums1[nums1_index]>nums2[j] :
                nums1[i] = nums1[nums1_index]
                i = i-1
            else:
                nums1[i] = nums2[j]
                j = j-1
                i = i-1