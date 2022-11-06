from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        course_map = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        link = [[] for _ in range(numCourses)]
        num_link = [0 for _ in range(numCourses)]

        for prereq in prerequisites:
            parent, chil = prereq
            link[parent].append(chil)
            num_link[chil] += 1
        
        q = deque()
        for i, n in enumerate(num_link):
            if n == 0:
                q.append(i)

    
        while len(q) > 0:
            idx = q.popleft()
            for i in link[idx]:
                num_link[i] -= 1
                if num_link[i] == 0:
                    q.append(i)
                course_map[idx][i] = True
                for j in range(numCourses):
                    if course_map[j][idx]:
                        course_map[j][i] = True
        answer = []
        for query in queries:
            start, end = query
            res = course_map[start][end]
            answer.append(res)

        return answer
