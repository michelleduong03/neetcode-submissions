from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)

        # result = heapq.nlargest(k, freq_map.keys())
        
        # return result
        return [item[0] for item in freq_map.most_common(k)]