class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(digit) for digit in digits]
        res = "".join(digits)
        sum = int(res) + 1

        ans = []
        for i in str(sum):
            ans.append(i)
        print(ans)
        return ans