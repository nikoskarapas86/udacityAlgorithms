from collections import deque


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_right_child(self):
        return self.right != None


# create a tree
class Tree():
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

# DFS


def pre_order(tree):
    visited_order = list()

    def traverse(node):
        if node:
            visited_order.append(node.get_value())

            traverse(node.get_left_child())
            traverse(node.get_right_child())
    traverse(tree.get_root())
    return visited_order

 # BFS algorithm


class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)


def bfs(tree):
    q = Queue()
    visit_order = list()
    node = tree.get_root()
    q.enq(node)
    while(len(q) > 0):
        node = q.deq()
        visit_order.append(node)
        if node.has_left_child():
            q.enq(node.get_left_child())
        if node.has_right_child():
            q.enq(node.get_right_child())

    return visit_order
