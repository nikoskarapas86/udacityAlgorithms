class Stack:
    def __init__(self):
        self.items = []

        # TODO: Initialize the Stack

    def size(self):
        return len(self.items)
        # TODO: Check the size of the Stack

    def push(self, item):
        # TODO: Push item onto Stack
        self.items.append(item)
        return self.items

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


MyStack = Stack()

MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print(MyStack.items)

MyStack.pop()
MyStack.pop()

print("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")

MyStack.pop()

print("Pass" if (MyStack.pop() == None) else "Fail")
