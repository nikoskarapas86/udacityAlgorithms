import sys


def getOccurences(str):
    tempDict = dict()
    for char in str:
        if char in tempDict:
            tempDict[char] += 1
        else:
            tempDict[char] = 1
    return tempDict


def getEncodedTree(sortedOccurences):
    _tree = dict()
    str = '1'
    for item in sortedOccurences:
        _tree[item[0]] = str
        str = '0' + str
    return _tree


def encodeWithHafman(data):
    encodedTree = {}
    occurences = getOccurences(data)
    sortedOccurences = sorted(
        occurences.items(), key=lambda occurence: occurence[1])
    encodedTree = getEncodedTree(sortedOccurences)
    return encodedTree


def getEncodedString(encodedTree, data):
    encodedStr = ""
    for item in data:
        encodedStr += encodedTree[item]
    return encodedStr


def getCharMapper(tree):
    mapper = dict()
    for node in tree:
        mapper[tree[node]] = node
    return mapper


def getDecodedStr(data, charMapper):
    decodedStr = ""
    str = ""
    for digit in data:
        if digit == '1':
            decodedStr += charMapper[str + digit]
            str = ''
        else:
            str += digit
    return decodedStr


def decodeWithHafman(data, tree):
    tempStr = ""
    charMapper = getCharMapper(tree)
    tempStr = getDecodedStr(data, charMapper)
    return tempStr


# test cases
if __name__ == "__main__":
    codes = {}

    bookTitle = "To kill a mockin bird"

    print("The size of the bookTitle is: {}\n".format(
        sys.getsizeof(bookTitle)))
    print("The content of the bookTitle is: {}\n".format(bookTitle))

    tree = encodeWithHafman(bookTitle)
    encodedString = getEncodedString(tree, bookTitle)
    print("The size of the encoded bookTitle is: {}\n".format(
        sys.getsizeof(int(encodedString, base=2))))
    print("The content of the encoded bookTitle is: {}\n".format(encodedString))

    decodedStr = decodeWithHafman(encodedString, tree)

    print("The size of the decoded bookTitle is: {}\n".format(
        sys.getsizeof(decodedStr)))
    print("The content of the decoded bookTitle is: {}\n".format(decodedStr))
