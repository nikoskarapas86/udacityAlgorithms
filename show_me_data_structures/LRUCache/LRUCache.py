class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cacheDic = dict()
        self.head = Node(0, 0)
        self.tail = self.head
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cacheDic:
            return -1
        else:
            node = self.cacheDic[key]
            self.delete_item(node)
            self.insert_item(node)
            return node.value

    def set(self, key, value):
        if self.capacity == 0:
            print("unable do any operations on 0 capacity")
        if key in self.cacheDic:
            self.delete_item(self.cacheDic[key])
        node = Node(key, value)
        self.insert_item(node)
        self.cacheDic[key] = node
        if len(self.cacheDic) > self.capacity:
            node = self.head.next
            self.delete_item(node)
            del self.cacheDic[node.key]

    def delete_item(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert_item(self, node):
        previous = self.tail.prev
        previous.next = node
        self.tail.prev = node
        node.prev = previous
        node.next = self.tail


# Test cases
print('First test case : ')
testCache1 = LRUCache(5)
testCache1.set(1, 1)
testCache1.set(2, 2)
testCache1.set(3, 3)
testCache1.set(4, 4)
print(testCache1.get(1))  # returns 1
print(testCache1.get(2))  # returns 2
print(testCache1.get(9))  # returns -1 because 9 is not present in the cache
testCache1.set(5, 5)
testCache1.set(6, 6)
print(testCache1.get(3))

print('second test case : ')
testCache2 = LRUCache(1)
testCache2.set(1, 1)
testCache2.set(2, 2)
print(testCache2.get(1))
print(testCache2.get(2))
testCache2.set(5, 5)
print(testCache2.get(5))
print(testCache2.get(6))

print('third test case :')
our_cache2 = LRUCache(0)
our_cache2.set(1, 1)
our_cache2.set(2, 2)
print(our_cache2.get(1))
print(our_cache2.get(2))
