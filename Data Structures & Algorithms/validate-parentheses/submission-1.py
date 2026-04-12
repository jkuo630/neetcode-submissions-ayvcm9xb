class Solution:
    def isValid(self, s: str) -> bool:
        paren_dict = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for paren in s:
            # if its an opening
            if paren in paren_dict.values():
                stack.append(paren)
            elif stack and paren_dict[paren] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0


            