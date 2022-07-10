
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def suffixes(self, suffix=''):
        if self.children is None:
            return []
        suffixes = []

        for character in self.children:

            if self.children[character].is_word:
                suffixes.append(suffix + character)

            suffixes += self.children[character].suffixes(
                suffix + character)

        return suffixes

    def insert(self, character):
        self.children[character] = TrieNode()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root

        for character in word:
            if character not in current_node.children:
                current_node.insert(character)
            current_node = current_node.children[character]
        current_node.is_word = True

    def find(self, prefix):
        node = self.root
        for character in prefix:
            if character in node.children:
                node = node.children[character]
            else:
                return TrieNode()
        return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
print("Test Case 0 edge case")
prefix = ''
prefixNode = MyTrie.find(prefix)
print("Prefix: '{}'".format(prefix))
print(prefixNode.suffixes())
print("Test Case 1")
prefix = 'an'
prefixNode = MyTrie.find(prefix)
print("Prefix: '{}'".format(prefix))
print(prefixNode.suffixes())

print("Test Case 2 ")
prefix = 'f'
prefixNode = MyTrie.find(prefix)
print("Prefix: '{}'".format(prefix))
print(prefixNode.suffixes())
# edge case
print("Test Case 4 edge case")
prefix2 = '111'
prefixNode = MyTrie.find(prefix2)
print("Prefix: '{}'".format(prefix2))
print(prefixNode.suffixes())
