class TimeMap:

    def __init__(self):
        self.time = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time:
            self.time[key] = []
        self.time[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:

        lst = self.time.get(key, [])
        ans = ""
        left = 0
        right = len(lst) - 1 
        
        while left <= right:
            mid = (left + right) // 2 
            # if current timestamp is valid (in the past or exact match)
            if lst[mid][0] <= timestamp:
                ans = lst[mid][1]   # temp store this as a potential answer
                left = mid + 1      # try to find a more recent (larger) valid time
            else:
                right = mid - 1

        return ans