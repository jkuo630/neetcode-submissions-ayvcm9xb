class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # complete adjacency list and indegree list
        # kahn's algorithm -> take course with 0 prerequisites, remove it from 
        # dependency lists of other courses 
        # if all courses can be taken, no cycle therefore true, else cycle exists 

        indegree = [0] * numCourses 
        adj = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            adj[prereq].append(course) # prereq -> course
            indegree[course] += 1 # course has one more dependency 

        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        finish = 0 
        while q:
            course = q.popleft()
            finish += 1 
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return finish == numCourses