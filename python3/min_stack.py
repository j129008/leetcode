class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x):
        self.stack.append(x)
        try:
            self.minStack.append(min(x, self.minTop()))
        except:
            self.minStack.append(x)

    def pop(self):
        self.minStack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def minTop(self):
        return self.minStack[-1]

    def getMin(self):
        return self.minStack[-1]

min_stack = MinStack()
min_stack.push(2)
min_stack.push(-1)
min_stack.push(-3)
min_stack.push(1)
min_stack.push(-2)
print(min_stack.pop())
print(min_stack.top())
print(min_stack.getMin())
print(min_stack.minStack)
print(min_stack.stack)
