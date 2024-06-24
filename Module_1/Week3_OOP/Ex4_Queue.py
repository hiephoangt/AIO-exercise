class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.lst = []

    def is_empty(self):
        if len(self.lst) == 0:
            return True
        return False

    def is_full(self):
        if len(self.lst) == self.capacity:
            return True
        return False

    def enqueue(self, item):
        if not self.is_full():
            self.lst.append(item)
        else:
            print("Don't enqueue")

    def dequeue(self):
        if not self.is_empty():
            self.lst.pop(0)
        else:
            print("Don't dequeue")

    def front(self):
        return self.lst[0]


if __name__ == "__main__":
    queue1 = MyQueue(5)
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)
    queue1.enqueue(4)
    queue1.enqueue(5)
    queue1.enqueue(6)
    print(queue1.front())
    queue1.dequeue()
    print(queue1.front())
