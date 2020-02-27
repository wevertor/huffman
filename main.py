import Node
import Letter


def huffman(path):
    """
        reads a file and build a bitstring for every letter
    """
    # create the list with letters
    letterList = Letter.build_list(path)

    # build the huffman tree
    root = Node.build_tree(letterList)

    # get the bitstring for each letter
    letters = Node.get_bitstring(root, "")

    # open the file
    with open(path) as f:
        with open("huffman.txt", "w") as h:
            while True:

                # read each character in the file
                c = f.read(1)

                # EOF
                if not c:
                    break

                # get the object Letter correspondent
                letter = list(filter(lambda l: l.ch == c, letters))[0]

                h.write(letter.bitstring)


if __name__ == "__main__":
    huffman("teste.txt")
