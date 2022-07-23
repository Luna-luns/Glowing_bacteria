class Strand:  # strand - single DNA chain
    def __init__(self, sequence: str):
        self.sequence = sequence

    def modify_strand(self) -> str:
        plasmid_dictionary = dict.fromkeys(self.sequence)
        plasmid_dictionary['T'] = 'A'
        plasmid_dictionary['A'] = 'T'
        plasmid_dictionary['C'] = 'G'
        plasmid_dictionary['G'] = 'C'

        return ''.join(plasmid_dictionary[char] for char in self.sequence)

    def get_first_strand(self) -> str:  # get it from input double-stranded plasmid sequence string
        return self.sequence.split()[0]

    def get_second_strand(self) -> str:  # get it from input double-stranded plasmid sequence string
        return self.sequence.split()[1]

    def find_original_index(self, restriction_site: str) -> int:
        return self.sequence.find(restriction_site)

    def find_complementary_index(self, restriction_site: str) -> int:
        return self.sequence.find(restriction_site[:-1]) + 4

    def cut_strand(self, index: int) -> str:
        return f'{self.sequence[:index + 1]} {self.sequence[index + 1:]}'
