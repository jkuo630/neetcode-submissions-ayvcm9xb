class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # look at it in reverse based on starting position
        # since cant look at it otherwise because 
        # we don't know if its going to become a car fleet or not 
        # add car to stack, calculate if its going to collide 
        # collide? t to target = remaining distance to target / speed 
        # if the car behind (top of the stack)
        # is faster or equal, than means its going to collide
        # so pop top of the stack, and put in new car into the stack 
        # at the end, return length of stack 

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []
        for p, s in pair:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
