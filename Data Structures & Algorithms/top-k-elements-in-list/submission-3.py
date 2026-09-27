class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_set = {}
        res = []

        for num in nums:
            if num in num_set:
                num_set[num] += 1
            else:
                num_set[num] = 1
        
        for x in range(k):
            num = max(num_set, key=num_set.get)
            res.append(num)
            del num_set[num]
        return res
