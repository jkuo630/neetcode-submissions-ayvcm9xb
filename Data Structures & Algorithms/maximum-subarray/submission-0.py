class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsf = nums[0]
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                maxsf = max(curr, maxsf)
        return maxsf