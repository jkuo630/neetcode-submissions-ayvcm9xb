class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiple everything, divide itself 
        # edge cases: 0 

        ans = []
        i = 0 
        while i < len(nums):
            temp = 1  
            for num in nums[:i]:
                temp *= num
            for num in nums[i+1:]:
                temp *= num
            ans.append(temp)
            i += 1 
        
        return ans
        