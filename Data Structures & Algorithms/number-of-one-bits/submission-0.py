class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_rep = bin(n)[2:] #binary rep and removing 0b bc binary
        count = 0
        
        for bit in binary_rep:
            if bit == '1':
                count += 1
        
        return count