# Trie is maintained as a dictionary
# with keys as letter or characters and value as Nodes
# Each node also contains dictionary to store children
class Trie:
    class TrieNode:
        def __init__(self, character):
            self.character = character
            self.children = {}
            self.wordEnd = False
            self.cnt = 1

        def __str__(self):
            def fun(node):
                output = []
                for key, child in node.children.items():
                    output.append(fun(child))
                return "<"+node.character+","+str(node.cnt)+">"+":" + "{" + " ".join(output) + "}"

            return fun(self)

    def __init__(self):
        self.root = Trie.TrieNode("")

    def __str__(self):
        return str(self.root)

    def insert(self, word):
        current = self.root
        for l in word:
            if l not in current.children.keys():
                current.children[l] = Trie.TrieNode(l)
            else:
                current.children[l].cnt += 1
            current = current.children[l]
        current.wordEnd = True

    def search(self, word):
        current = self.root
        for l in word:
            if l not in current.children.keys():
                return False
            current = current.children[l]
        return current.wordEnd

    def startsWith(self, prefix):
        current = self.root
        for l in prefix:
            if l not in current.children.keys():
                return False
            current = current.children[l]
        return True


# Driver Code
trie = Trie()
trie.insert("apple")
trie.insert("apple")
trie.insert("mango")
trie.insert("banana")
print(trie)
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
