class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # n -> cooldown period 
        # tasks = ["X","X","Y","Y"], n = 2 
        # 12idle45 

        # want to run the most frequent task first 
        # maxheap based on frequency 
        # queue to keep track of things on cooldown (remaining_time, next_avail)

        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)

        time = 0 
        q = deque() # [-count, remaining_time]
        while heap or q:
            time += 1 
            # if there are things in the heap 
            if heap:
                counter = 1 + heapq.heappop(heap)
                if counter < 0:
                    q.append([counter, time + n])
            # go to the queue 
            else:
                time = q[0][1]

            # if we can use things from the cooldown queue, 
            # push it to the heap 
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time

        