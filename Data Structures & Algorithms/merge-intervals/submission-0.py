class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn)
        intervals.sort(key=lambda i : i[0]) # sprt by start vla
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1] # end value

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        
        return output
            