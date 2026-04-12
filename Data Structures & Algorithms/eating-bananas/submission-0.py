class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles = [1,4,3,2], h = 9
        # output -> min rate at which we want to eat at to eat all bananas
        # 1 -> 10 hrs -> not valid
        # 2 -> 6 hrs -> ans 
        # 3 -> 5 hrs 

        # brute force -> start from 1 -> calculate each time, until its 
        # valid 
        # max(piles) -> o(n)
        # o(n^2)

        # map all the rates of speed -> valid 
        # 1 -> max(piles)
        # binary search speeds -> until we find a speed that is valid 
        # ascending order -> binary search 
        # [1,2,3,4,5] -> 3, not valid -> look higher, valid -> look lower -> min 
        # at the very end, return min 

        # min counter  
        # o(n)

        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2 
            
            totalTime = 0 
            for p in piles:
                totalTime += math.ceil(p / mid)

            if totalTime <= h:
                ans = mid       
                right = mid - 1 
            else:
                left = mid + 1  
        
        return ans