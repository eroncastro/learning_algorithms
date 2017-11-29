class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0] if any(self.storage) else None

    def dequeue(self):
        return self.storage.pop(0)
