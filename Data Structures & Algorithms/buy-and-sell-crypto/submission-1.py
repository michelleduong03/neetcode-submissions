class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_prof = 0

        while right < len(prices):
            curr = prices[right] - prices[left]

            if prices[right] > prices[left]:
                max_prof = max(curr, max_prof)
            else:
                left = right
            
            right += 1

        return max_prof