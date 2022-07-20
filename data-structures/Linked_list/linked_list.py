class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)
        return self.head

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def to_list(self):
        if self.head is None:
            return []
        else:
            list_of_values = []
            current = self.head
            while current:
                list_of_values.append(current.value)
                current = current.next
            return list_of_values

    def search(self, value):

        if self.head is None:
            return None

        temp = self.head
        while temp:
            if temp.value == value:
                return temp
            temp = temp.next
        return -1

    def remove(self, value):
        if self.head is None:
            return None
        if self.head.value == value:
            tempo = self.head
            self.head = self.head.next
            tempo.next = None
            return True
        temp = self.head
        while temp.next:
            if temp.next.value == value:
                temp.next = temp.next.next
                return True
            temp = temp.next
        return False

    def reverseLinkedList(self):

        if self.head is None:
            return None
        reversedList = reversed(self.to_list())
        reversedLinkedList = LinkedList()
        for value in reversedList:
            reversedLinkedList.append(value)
        return reversedLinkedList

    def isSyrcular(self):
        if self.head is None:
            return False
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


linked_list = LinkedList()
# print(linked_list.append(3).value)
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.prepend(8)


reversedd = linked_list.reverseLinkedList()
print(reversedd.head.value)


def merge(list1, list2):
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt is not None or list2_elt is not None:
        if list1_elt is None:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
    return merged
