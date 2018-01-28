class TrieNode:

    def __init__(self, isLeaf):
        self.isLeaf = isLeaf
        self.next = {}
    def insert(self, val, isLeaf):
    	self.next[val] = TrieNode(isLeaf)
    	return self.next[val] 

class Trie:
	def __init__(self):
	   self.root = TrieNode(self, isLeaf)

	def add_word(self, new_word):
        i = 0
        node = self.root
        while i < len(new_word):
            curr = new_word[i]
            if curr not in node.next:
                node.next[curr] = TrieNode(i == len(new_word) - 1)
                node = node.next[curr]
            i += 1

	def check(self, word):


