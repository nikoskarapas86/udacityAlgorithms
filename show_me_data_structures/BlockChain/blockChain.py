import datetime
import hashlib


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def calc_hash(self, str):
        sha = hashlib.sha256()
        sha.update(str.encode('utf-8'))
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.tail = None
        self.numOfBlocks = 0

    def getCurrentDateTime(self):
        return datetime.datetime.now()

    def append(self, data):
        if self.tail == None:
            self.tail = Block(self.getCurrentDateTime(), data, None)
        else:
            self.tail = Block(self.getCurrentDateTime(), data, self.tail)
        self.numOfBlocks += 1

    def getSize(self):
        return self.numOfBlocks

    def search(self, data):
        if self.tail is None:
            return None
        else:
            temp = self.tail
            while temp.previous_hash:
                if temp.data == data:
                    return data
                else:
                    temp = temp.previous_hash
        return None

    def convertBlockChainToList(self):
        listBlockChain = []
        block = self.tail
        while block:
            listBlockChain.append(block.data)
            block = block.previous_hash
        return listBlockChain


print("test case 1")
blockChain = BlockChain()
print(blockChain.getSize())
print(blockChain.convertBlockChainToList())
print("test case 2")
blockChain1 = BlockChain()
blockChain1.append("first block in chain")
blockChain1.append("second block in chain")
print(blockChain1.getSize())
print(blockChain1.convertBlockChainToList())
print(blockChain1.search("second block in chain"))
