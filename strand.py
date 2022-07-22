class Strand:  # strand - single DNA chain
    RESTRICTION_SITE = 'CTGCAG'

    def __init__(self, sequence: str):
        self.sequence = sequence

    def modify_strand(self) -> str:
        plasmid_dictionary = dict.fromkeys(self.sequence)
        plasmid_dictionary['T'] = 'A'
        plasmid_dictionary['A'] = 'T'
        plasmid_dictionary['C'] = 'G'
        plasmid_dictionary['G'] = 'C'

        return ''.join(plasmid_dictionary[char] for char in self.sequence)

    def get_original_strand(self) -> str:  # get it from input double-stranded plasmid sequence string
        return self.sequence.split()[0]

    def get_complementary_strand(self) -> str:  # get it from input double-stranded plasmid sequence string
        return self.sequence.split()[1]

    def find_original_index(self) -> int:
        return self.sequence.find(self.RESTRICTION_SITE)

    def find_complementary_index(self) -> int:
        return self.sequence.find(self.RESTRICTION_SITE[::-1]) + 4

    def cut_strand(self, index: int) -> str:
        return f'{self.sequence[:index + 1]} {self.sequence[index + 1:]}'

    def combine_original_complementary_strands(self) -> str:  # now we don't need it
        complementary_strand = self.modify_strand()
        return f'{self.sequence} {complementary_strand}'
