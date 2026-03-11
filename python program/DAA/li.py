class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

        print(f"{temp.data} removed")

    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Front element:", self.front.data)

    def display(self):
        temp = self.front
        print("Queue:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
# Driver Code
q = QueueLinkedList()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

q.dequeue()
q.peek()
q.display()
