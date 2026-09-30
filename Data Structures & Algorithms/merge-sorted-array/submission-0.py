class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
       
        left = nums1[:m] 
        right = nums2
        i, j, k = 0, 0, 0 

        while j < m and k < n:
            if left[j] <= right[k]:
                nums1[i] = left[j]
                j += 1
            else:
                nums1[i] = right[k]
                k += 1
            i += 1

        while j < m:
            nums1[i] = left[j]
            j += 1
            i += 1
        while k < n:
            nums1[i] = right[k]
            k += 1
            i += 1