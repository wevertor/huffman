from Letter import Letter


class TreeNode(object):
    def __init__(self, freq, left, right):
        self.freq = freq
        self.left = left
        self.right = right

    def __repr__(self):
        return "Node:"+str(self.freq)


def build_tree(lettersList):
    '''
    Run through the list of letters and build the min heap
    for the huffman tree.
    '''
    while len(lettersList) > 1:

        # pick the first two letters with minor frequency
        left = lettersList.pop(0)
        right = lettersList.pop(0)

        # sum the frequencies to get the father's frequency
        totalFreq = left.freq + right.freq

        # create a new node
        node = TreeNode(totalFreq, left, right)

        # store the new node in list
        lettersList.append(node)

        # sort by frequency
        lettersList.sort(key=lambda l: l.freq)

    return lettersList[0]


def get_bitstring(root, bitstring):
    """
    go recursively through the tree and set the bitstring
    for each letter and return the list of letters
    """
    # if the root is a letter, then return itself
    if type(root) is Letter:
        root.bitstring = bitstring
        return [root]

        # if the root is a tree node, access recursively the children
    letters = []
    letters += get_bitstring(root.left, bitstring + "0")
    letters += get_bitstring(root.right, bitstring + "1")

    return letters
