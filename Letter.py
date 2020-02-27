import Node


class Letter(object):
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.bitstring = ""

    def __repr__(self):
        return str(self.char)+":"+str(self.freq)


def build_list(path):
    """
    Read a text file and build a dict of all letters and
    their frequencies, then return a list with the Letters
    ordened by their frequencies.
    """

    chars = {}
    with open(path) as f:
        while True:

            # read a character
            buffer = f.read(1)

            # if EOF stop
            if not buffer:
                break

            # store the character
            if buffer in chars.keys():
                chars[buffer] = chars[buffer] + 1
            else:
                chars[buffer] = 1

    # create the list ordened by the frequency
    return sorted([Letter(ch, freq) for ch, freq in chars.items()],
                  key=lambda l: l.freq)


if __name__ == "__main__":
    Node.build_tree(build_list("teste.txt"))
