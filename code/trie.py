class Node:
    def __init__(self):
        self.next = {}
        self.count = 0
    def insert(self, word, i):
        if i == len(word):
            self.count += 1
            return self.count
        next = word[i]
        if next not in self.next:
            self.next[next] = Node()
        self.count += 1
        return self.next[next].insert(word, i+1)

class Trie(Node):
    def __init__(self):
        super().__init__()
    def insert(self, word):
        return super().insert(word, 0)