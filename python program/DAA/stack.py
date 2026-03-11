class Stack:
    def create_stack(self, max_size):
        self.items = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.max_size

    def push(self, item):
        if self.is_full():
            print("Stack Overflow! Cannot push element.")
        else:
            self.items.append(item)
            print(f"Pushed {item} into stack")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop element.")
        else:
            popped = self.items.pop()
            print(f"Popped element is {popped}")

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print(f"Top element is {self.items[-1]}")

    def size(self):
        print(f"Stack size is {len(self.items)}")
s = Stack()
s.create_stack(3)   # Maximum size = 3

s.push(10)
s.push(20)
s.push(30)
s.push(40)          # Overflow condition

s.peek()
s.size()

s.pop()
s.pop()
s.pop()
s.pop()             # Underflow condition
