class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item} into queue")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty. Cannot dequeue.")
        else:
            print(f"Dequeued {self.queue.pop(0)} from queue")

    def front(self):
        if self.isEmpty():
            print("Queue is empty.")
        else:
            print(f"Front element is {self.queue[0]}")

    def size(self):
        print(f"Queue size is {len(self.queue)}")


# Driver Code
q = Queue()
q.enqueue(5)
q.enqueue(15)
q.enqueue(25)
q.front()
q.dequeue()
q.size()
