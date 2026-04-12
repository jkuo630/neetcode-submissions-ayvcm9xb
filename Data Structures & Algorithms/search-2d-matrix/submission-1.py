class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # can iterate through each list, and do binary search on it 
        # o(n^2)
        # def binarySearch(nums: List[int]) -> int:
        #     left = 0 
        #     right = len(nums) - 1

        #     while left <= right:
        #         mid = (left + right) // 2
        #         if nums[mid] > target:
        #             right = mid - 1
        #         elif nums[mid] < target:
        #             left = mid + 1 
        #         else:
        #             return mid
            
        #     return -1
        
        # for lst in matrix:
        #     if binarySearch(lst) != -1:
        #         return True 
        
        # return False

        # optimal solution -> binary search to correct list 
        # then binary search again within that list 

        if not matrix or not matrix[0]: return False
        
        # 1. Binary Search to find the potential row
        top = 0
        bot = len(matrix) - 1
        row = 0
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]: 
                top = mid + 1
            elif target < matrix[mid][0]: 
                bot = mid - 1
            else:
                row = mid 
                break

        # 2. Binary Search within that specific row
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        
        return False