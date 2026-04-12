class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force, for each temp -> iterate the rest of the temps 
        # to see when the closest warmer day is 
        # o(n^2)

        
        # optimal -> use monotonically decreasing stack 
        # keep track of temp and index 
        # if the curr temp is greater than top of the stack, 
        # calculate the diff between that index and curr index 
        # add that to the ans 
        # keep popping till it isnt 

        ans = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                currI, currT = stack.pop()
                ans[currI] = i - currI
            stack.append((i, temp))
        
        return ans