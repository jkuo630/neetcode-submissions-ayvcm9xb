class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort based on first item 
        # iterate through list
        # if end is greater than start, merge, take start of first, and 
        # end of second 

        intervals.sort(key=lambda pair: pair[0])
        ans = [intervals[0]]

        for start, end in intervals:
            lastEnd = ans[-1][1]
            if start <= lastEnd:
                ans[-1][1] = max(lastEnd, end)
            else:
                ans.append([start, end])
        
        return ans 
