from queue import Queue

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prevs = dict()
        nexts = dict()
        for n in range(numCourses):
            prevs[n] = []
            nexts[n] = []
        
        for p, c in prerequisites:
            prevs[p].append(c)
            nexts[c].append(p)
            
        roots = []
        for n in range(numCourses):
            if len(prevs[n]) == 0:
                roots.append(n)
        # print(roots)
        if len(roots) == 0:
            return []
        
        answer = []
        used = [False for _ in range(numCourses)]
        q = Queue()
        for r in roots:
            q.put(r)
        # print(prevs)
        # print(nexts)
        while not q.empty():
            r = q.get()
            if used[r] == False:
                answer.append(r)
                used[r] = True
            for i in nexts[r]:
                is_i_use = True
                for j in prevs[i]:
                    if used[j] == False:
                        is_i_use = False
                if is_i_use:
                    q.put(i)
        
        if len(answer) != numCourses:
            return []
        
        return answer
            