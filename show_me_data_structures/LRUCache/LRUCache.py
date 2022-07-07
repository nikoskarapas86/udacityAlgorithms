class DLLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cacheDic = dict()
        self.head = DLLNode(0, 0)
        self.tail = self.head
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cacheDic:
            return -1
        else:
            node = self.cacheDic[key]
            self.delete_least_recent(node)
            self.insert_new_item(node)
            return node.value

    def set(self, key, value):
        if key in self.cacheDic:
            self.delete_least_recent(self.cacheDic[key])
        node = DLLNode(key, value)
        self.insert_new_item(node)
        self.cacheDic[key] = node
        if len(self.cacheDic) > self.capacity:
            node = self.head.next
            self.delete_least_recent(node)
            del self.cacheDic[node.key]

    def delete_least_recent(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert_new_item(self, node):
        prevs = self.tail.prev
        prevs.next = node
        self.tail.prev = node
        node.prev = prevs
        node.next = self.tail


# Tests
# Testcase 1
print('***** Testcase 1 *****')
our_cache1 = LRUCache(5)
our_cache1.set(1, 1)
our_cache1.set(2, 2)
our_cache1.set(3, 3)
our_cache1.set(4, 4)
print(our_cache1.get(1))  # returns 1
print(our_cache1.get(2))  # returns 2
print(our_cache1.get(9))  # returns -1 because 9 is not present in the cache
our_cache1.set(5, 5)
our_cache1.set(6, 6)
# returns -1 because the cache reached it's capacity and 3 was the LRU entry
print(our_cache1.get(3))

# Testcase 2
print('***** Testcase 2 *****')
our_cache2 = LRUCache(1)
our_cache2.set(1, 1)
our_cache2.set(2, 2)
print(our_cache2.get(1))
print(our_cache2.get(2))
our_cache2.set(5, 5)
print(our_cache2.get(5))
print(our_cache2.get(6))

# Testcase 3
print('***** Testcase 3 *****')
our_cache2 = LRUCache(3)
our_cache2.set(1, 1)
our_cache2.set(2, 2)
print(our_cache2.get(1))
print(our_cache2.get(2))
our_cache2.set(5, 5)
print(our_cache2.get(5))
print(our_cache2.get(6))
