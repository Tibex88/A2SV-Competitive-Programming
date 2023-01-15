# https://leetcode.com/problems/task-scheduler/submissions/878631983/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                val = 1 + heapq.heappop(maxHeap)
                if val:
                    q.append([val, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])    
        return time