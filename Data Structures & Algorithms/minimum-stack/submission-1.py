class MinStack:

    def __init__(self):
        self.stack = []
        self.smallstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.smallstack:
            self.smallstack.append(val)
        else:
            self.smallstack.append(min(val, self.smallstack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.smallstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallstack[-1]
        
