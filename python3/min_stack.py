class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        try:
            self.stack.append((x, min(x, self.getMin())))
        except:
            self.stack.append((x, x))

    def pop(self):
        return self.stack.pop()[0]

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]

min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(1)
print(min_stack.getMin())
