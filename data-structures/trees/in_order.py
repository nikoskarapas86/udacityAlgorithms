

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# time complexity O(n) space complexity O(n)


def in_order(root):
    if root is None:
        return []
    current = root
    stack = []
    while True:
        if current is not None:
            stack.push(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.data)
            current = current.right
        else:
            break
