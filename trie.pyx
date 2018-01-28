cdef class TrieNode:

    string val
    bool isLeaf
    dict next

    def __init__(self, bool isLeaf):
        self.isLeaf = isLeaf
        self.next = {}
    def insert(self, string val, bool isLeaf):
    	self.next[val] = TrieNode(isLeaf)
    	return self.next[val] 

cdef class Trie:
	TrieNode root

	def __init__(self):
		self.root = TrieNode(self, __, isLeaf)

	def add_word(self, string new_word):
		int i = 0;
		

	def check(self, string word):
		int i = 0;


