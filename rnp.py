# https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/878605665/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        operators = ["+","-","*","/"]
        
        for t in tokens:
            if t in operators:
                if t == "+":
                   arr.append(int(arr.pop()) + int(arr.pop()))
                if t == "-":
                   a, b= arr.pop(), arr.pop()
                   arr.append(int(b)-int(a))
                if t == "*":
                   arr.append(int(arr.pop()) * int(arr.pop()))
                if t == "/":
                    a, b= arr.pop(), arr.pop()
                    arr.append(int(int(b)/int(a)))
            else:
                arr.append(int(t))

        return arr[0]
            