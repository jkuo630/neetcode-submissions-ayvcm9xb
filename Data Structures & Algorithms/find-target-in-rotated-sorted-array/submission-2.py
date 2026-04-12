class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search 
        # two sorted arrays -> array 1 > array 2 
        # target is greater than left, right -> mid - 1 
        # else left -> mid + 1 

        # nums = [3,4,5,6,7,1,2], target = 1


        left = 0 
        right = len(nums) - 1 

        while left <= right:
            mid = (left + right) // 2 
            if nums[mid] == target:
                return mid 

            # left portion? 
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1 
                else:
                    right = mid - 1
            # right portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1 
                else:
                    left = mid + 1 


        return -1 