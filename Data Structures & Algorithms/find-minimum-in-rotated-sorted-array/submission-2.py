class Solution:
    def findMin(self, nums: List[int]) -> int:
        # can think of it as 2 sorted arrays once it rotates 
        # want to search in the smaller one
        # we can use the left or right pointers to tell which 
        # array we are in. if the curr num is greater than the left pointer num, 
        # then its in the bigger array 
        
        left = 0 
        right = len(nums) - 1 
        ans = nums[0]

        
        while left <= right:
            if nums[left] < nums[right]:
                ans = min(ans, nums[left])

            mid = (left + right) // 2 
            ans = min(ans, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1 
            elif nums[mid] <= nums[left]:
                right = mid - 1
            
        return ans
        
