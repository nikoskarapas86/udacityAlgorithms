class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):

    if llist_1.head is None and llist_2.head is None:
        return None
    unionLinkedList = LinkedList()
    unionSet = set()
    temp1 = llist_1.head
    # O(n)
    while temp1.next:
        unionSet.add(temp1.value)
        temp1 = temp1.next
    temp2 = llist_2.head
    # O(n)
    while temp2.next:
        unionSet.add(temp2.value)
        temp2 = temp2.next
     # O(n)
    for item in unionSet:
        unionLinkedList.append(item)
    return unionLinkedList


def intersection(llist_1, llist_2):
    if llist_1.head is None and llist_2.head is None:
        return None
    intersectionLL = LinkedList()
    set1 = set()
    temp1 = llist_1.head
    # O(n)
    while temp1.next:
        set1.add(temp1.value)
        temp1 = temp1.next
    set2 = set()
    temp2 = llist_2.head
    # O(n)
    while temp2.next:
        set2.add(temp2.value)
        temp2 = temp2.next
    # O(n)
    for item in set1:
        if item in set2:
            intersectionLL.append(item)
    return intersectionLL


print("test case 1")
llist_1 = LinkedList()
llist_2 = LinkedList()

l1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
l2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for item in l1:
    llist_1.append(item)

for item in l2:
    llist_2.append(item)

print(union(llist_1, llist_2))
print(intersection(llist_1, llist_2))
