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
