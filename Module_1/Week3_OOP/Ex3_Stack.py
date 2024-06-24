class Stack:
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

    def pop(self):
        if not self.is_empty():
            self.lst.pop(-1)
        else:
            print("Don't pop")

    def push(self, item):
        if not self.is_full():
            self.lst.append(item)
        else:
            print("Don't push")

    def top(self):
        return self.lst[-1]


if __name__ == "__main__":
    stack1 = Stack(5)
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)
    stack1.push(5)
    stack1.push(6)
    print(stack1.top())
    stack1.pop()
    print(stack1.top())
    stack1.is_empty()
