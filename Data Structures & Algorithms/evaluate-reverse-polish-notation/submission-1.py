class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        ops = {'+', '-', '*', '/'}
        for t in tokens:    
            if t not in ops:
                s.append(int(t))
            else:
                if t == '+': s.append(s.pop() + s.pop())
                if t == '-':
                    a = s.pop()
                    b = s.pop()
                    s.append(b - a)
                if t == '*': s.append( s.pop() * s.pop())
                if t == '/':
                    a = s.pop()
                    b = s.pop()
                    s.append(int(b / a))
        return int(s.pop())
