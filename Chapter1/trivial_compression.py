# trivial_compression.py
class CompressedGene:
    MAP = {
        'A': 0b00,
        'C': 0b01,
        'G': 0b10,
        'T': 0b11,
    }
    def __init__(self, gene):
        self.gene = gene
        self.compres()

    def compres(self):
        self.bit_string = 1
        for n in self.gene.upper():
            self.bit_string <<= 2
            self.bit_string |= self.MAP[n]

    def decompress(self):
        """
        At the end of compress method, we would save an integer number
        in self.bit_string. There is this 'bin' function in python, by which you could pass
        an integer number and it would return the binary representation of that number, like:
        bin(12)
        >>'0b1100'
        So, we could solve the decompress by using this function, just skip the
        first 3 characters
        string = bin(self.bit_string)[3:]
        now, we can split the string by two characters and each group represents a nucleotide.
        """
        reverse_map = {v: k for k, v in self.MAP.items()}
        gene = ''
        for i in range(0, self.bit_string.bit_length() -1, 2):
            bits = self.bit_string >> i & 0b11
            gene += reverse_map[bits]
        return gene[::-1]

    def __str__(self) -> str:  # string representation for pretty printing
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)  # compress
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed)  # decompress
    print("original and decompressed are the same: {}".format(original == compressed.decompress()))
