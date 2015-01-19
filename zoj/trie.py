


class Node:
	def __init__(self):
		self.word = None
		self.children = {}

class Trie:
	def __init__(self):
		self.root = Node()

	def insert(self,word):
		node = self.root
		for ch in word:
			if ch not in node.children:
				node.children[ch] = Node()
			node = node.children[ch]
		node.word = word

	def search(self,word):
		node = self.root
		for ch in word:
			if ch in node.children:
				node = node.children[ch]
			else:
				return False,none
		return True,node.word

	def is_contain(self,text):
		node = self.root
		if not node.children:
			return False,-1,-1

		for i in range(len(text)):
			while j < len(text) and any(node.childern) and text[i] in node.children:
				j = j + 1
				node = node.children
			if not node.children:
				return True,i,j
		return False,-1,-1

	def delete(self,word):
		pass


