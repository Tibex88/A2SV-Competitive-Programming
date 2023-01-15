# https://leetcode.com/problems/validate-stack-sequences/submissions/878645354/


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i= 0
        N = len(popped)

        for p in pushed:
            stack.append(p)
            print("push", stack)
            while stack and i<N and stack[-1] == popped[i]:
                i+=1
                stack.pop()
        return stack == []
            