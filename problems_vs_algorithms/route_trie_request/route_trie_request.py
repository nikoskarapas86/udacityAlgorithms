class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None
# time complexity O( 1) space complexity O(1)

    def insert(self, path):
        self.children[path] = RouteTrieNode()


class RouteTrie:
    def __init__(self, handler, error):
        self.root = RouteTrieNode()
        self.root.handler = handler
        self.error = error
# time complexity O(n) space complexity O(1)

    def insert(self, listOfPaths, handler):
        if listOfPaths == []:
            return False
        node = self.root
        for path in listOfPaths:
            if path not in node.children:
                node.insert(path)
            node = node.children[path]
        node.handler = handler
        return True
# time complexity O(n) space complexity O(1)

    def find(self, path_list):
        if len(path_list) == 0:
            return None

        if path_list == ['/']:
            return self.root.handler
        node = self.root
        for part in path_list:
            if part in node.children:
                node = node.children[part]
            else:
                return self.error

        if node.handler:
            return node.handler
        else:
            return self.error


class Router:
    def __init__(self, handler=None, error=None):
        self.root = RouteTrie(handler, error)
# time complexity O(1) space complexity O(1)

    def add_handler(self, path, handler):
        path_list = self.split_path(path)
        return self.root.insert(path_list, handler)
# time complexity O(n) space complexity O(1)

    def lookup(self, path):
        path_list = self.split_path(path)
        return self.root.find(path_list)

    def split_path(self, path):
        if path == "":
            return []

        if path == "/":
            return ["/"]

        return path.strip('/').split('/')


router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route
print("test case 1")
# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print("test case 2")
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print("test case 3")
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
print("test case 4")
router1 = Router("another handler", "not found another handler")
router1.add_handler("/another", "something handler")
router1.add_handler("/another/test", "about test handler")  # add a route
print(router1.lookup("/another"))
print(router1.lookup("/another/"))
print(router1.lookup("/another/test"))
