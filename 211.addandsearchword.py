def __init__(self):
	self.words = collections.defaultdict(list)
	
def addword(self, word):
	self.words[len(word)].append(word)
	
def search(self, word):
	if len(self.words[len(word)]) == 0:
		return False
	for w in self.words[len(word)]:
		for i in range(len(w)):
			if word[i] != '.' and word[i] != w[i]:
				break
			elif i == len(w) - 1
				return True
	return False
