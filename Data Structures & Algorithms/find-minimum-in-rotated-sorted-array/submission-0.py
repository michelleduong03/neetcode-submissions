class Solution:
    def findMin(self, nums: List[int]) -> int:
        # min_num = 1000
        # for i in range(len(nums)):
        #     curr_num = nums[i]
        #     if curr_num < min_num:
        #         min_num = curr_num
        # return min_num
        # return min(nums)
        # nums.sort()
        
        # return nums[0]

        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res