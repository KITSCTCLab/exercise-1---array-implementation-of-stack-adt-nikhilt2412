class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size
        self.top = 0

    def is_empty(self):
        if self.top == 0:
            return true
        else:
            return false

    def is_full(self):
        if self.top == (self.size - 1):
            return true
        else:
            return false

    def push(self, data):
        if not self.is_full():
            # Write code here

    def pop(self):
        if self.is_empty():
            # Write code here

    def status(self):
        # Write code here

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
