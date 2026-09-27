class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # initial val of 1
        pre = 1

        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums) - 1, -1, -1): # start @ end up to beginning of arr
            res[i] *= post
            post *= nums[i]
        return res
            