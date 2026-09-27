class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # numSet = set()

        # for n in nums:
        #     if n in numSet:
        #         return n
        #     numSet.add(n)
        # return 0 # TC: O(n) SC: O(n)
        slow, fast = 0, 0
        # finds their intersection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # 2x

            if slow == fast:
                break
            
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow #O(n) + O(1)