class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force -> check max function 
        # window, every iteration, check max 
        # o(n) x o(n) -> o(n^2)

        # check max for the first one, 
        # everytime we slide the window -> introducing, one new element 
        # check if that new element is greater than the current max 

        # o(n) + o(n) -> o(n)

        # keep a max heap of the numbers 
        # top one is the max 
        # pop the left one and push the right one everytime the window slides 
        # peek at the top to add it to the ans list 


        max_heap = []
        ans = []

        for right in range(len(nums)):
            heapq.heappush(max_heap, (-nums[right], right))
            if right >= k - 1:
                while max_heap[0][1] <= right - k:
                    heapq.heappop(max_heap)
                ans.append(-max_heap[0][0])


        return ans