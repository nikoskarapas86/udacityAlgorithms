class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = DoubleNode(value)
        if self.head is None:
            self.head = node
            self.tail = self.head
            return self
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        return self


linked_list = DoubleLinkedList()
linked_list.append(1)
linked_list.append(-2)
linked_list.append(4)

node = linked_list.head
while node:
    print(node.value)
    node = node.next
