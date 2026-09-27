class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashset = set() # allow to insert in O(1) time and check if certain value exists

        # for i in nums:
        #     if i in hashset:
        #         return True
        #     hashset.add(i)
        # return False

        return len(nums) != len(set(nums))