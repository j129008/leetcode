class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)

min_stack = MinStack()
min_stack.push(2)
min_stack.push(-1)
min_stack.push(-3)
min_stack.push(1)
min_stack.push(-2)
print(min_stack.pop())
print(min_stack.top())
print(min_stack.getMin())
