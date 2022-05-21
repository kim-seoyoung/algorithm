class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:

    def __init__(self):
        self.head = Node(None)

    def insert(self, word: str) -> None:
        len_word = len(word)
        
        curr_head = self.head
        for i in range(len_word):
            if not curr_head.children.get(word[i]):
                curr_head.children[word[i]] = Node(word[i])
                
            curr_head = curr_head.children[word[i]]
            if i == len_word -1:
                curr_head.data = word
                
            print(curr_head.key)
        

    def search(self, word: str) -> bool:
        curr_head = self.head
        for w in word:
            if not curr_head.children.get(w):
                return False
            
            curr_head = curr_head.children.get(w)
        
        if curr_head.data == word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr_head = self.head
        for w in prefix:
            if curr_head.data == prefix:
                return True
            
            if not curr_head.children.get(w):
                return False
            
            curr_head = curr_head.children.get(w)
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)