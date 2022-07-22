
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None


class Tree:
    def __init__(self):
        self.list = list()

# pre order traversion


def pre_order(tree):
    visit_order = list()

    def traverse(node):
        if node:
            visit_order.append(node.get_value())
            traverse(node.get_left_child())
            traverse(node.get_right_child())
    traverse(tree.get_root())
    return visit_order

# in order traversion


def in_order(tree):
    visit_order = list()

    def traverse(node):
        if node:
            traverse(node.get_left_child())
            visit_order.append(node.get_value())
            traverse(node.get_right_child())
    traverse(tree.get_root())
    return visit_order
# post order traversion


def post_order(tree):
    visit_order = list()

    def traverse(node):
        if node:
            traverse(node.get_left_child())
            traverse(node.get_right_child())
            visit_order.append(node.get_value())
    traverse(tree.get_root())
    return visit_order
