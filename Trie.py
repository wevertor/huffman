class TrieNode(object):
    def __init__(self, numberOfCharacters=2):
        self.children = [None]*numberOfCharacters

        self.isEndOfWord = False


class Trie(object):
    def __init__(self, numberOfCharacters=2):
        self.numberOfCharacters = numberOfCharacters
        self._root = self._getNode()

    def _getNode(self):
        # returns a new trie node empty
        return TrieNode(self.numberOfCharacters)

    def _charToIndex(self, ch):
        # returns true if the character is 1
        return int(ch)

    def insert(self, key):

        cur = self._root

        # iterate over the tree
        for _, ch in enumerate(key):
            childrenIndex = self._charToIndex(ch)

            # if the current character is not present
            if not cur.children[childrenIndex]:
                # create a new node
                cur.children[childrenIndex] = self._getNode()

            cur = cur.children[childrenIndex]

        cur.isEndOfWord = True

    def search(self, key):
        cur = self._root

        # iterate over the tree
        for _, ch in enumerate(key):
            childrenIndex = self._charToIndex(ch)

            # returns false if the current character is not present
            if not cur.children[childrenIndex]:
                return False

            cur = cur.children[childrenIndex]

        # returns true if the word is present
        return bool(cur != None and cur.isEndOfWord)
