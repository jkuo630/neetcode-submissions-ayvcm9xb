class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # brute force 
        # ans = []
        # i = 0 
        # while i < len(nums):
        #     temp = 1  
        #     for num in nums[:i]:
        #         temp *= num
        #     for num in nums[i+1:]:
        #         temp *= num
        #     ans.append(temp)
        #     i += 1 
        
        # return ans

        # optimized solution
        # build a prefix product list 
        # build a postfix product list 
        # build a result list 
        
        # n = len(nums)
        # ans = [1] * n 
        # prefix = [1] * n
        # postfix = [1] * n 
        
        # for i in range(1, n):
        #     prefix[i] = nums[i - 1] * prefix[i - 1]
        # for i in range(n - 2, -1, -1):
        #     postfix[i] = nums[i + 1] * postfix[i + 1]
        # for i in range(n):
        #     ans[i] = prefix[i] * postfix[i]
        
        # return ans

        # giga optimized solution 
        # do the same thing, but with one list. 2 passes, prefix first, postfix, then return it 

        n = len(nums)
        ans = [1] * n  
        # prefix
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
        # postfix + ans 
        postfix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= postfix 
            postfix *= nums[i]
        
        return ans 

        


        