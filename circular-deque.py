# https://leetcode.com/problems/design-circular-deque/submissions/878617182/

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.q = deque([],maxlen=k)

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.q.appendleft(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull()  :
            self.q.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.q.popleft()
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.q.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.q[0]
        else:
            return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.q[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if len(self.q)==0:
             return True
        else:
            return False

    def isFull(self) -> bool:
        if len(self.q)== self.k:
             return True
        else:
            return False
