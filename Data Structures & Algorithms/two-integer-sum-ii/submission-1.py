class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # double for loop 
        # pointer on one, -> next pointer iterates through the rest, looking for a num = to the diff 

        i = 0 
        while i < len(numbers):
            diff = target - numbers[i]
            for j in range(i + 1, len(numbers)):
                if numbers[j] == diff:
                    return [i + 1, j + 1]

            i += 1