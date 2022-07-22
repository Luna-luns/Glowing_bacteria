from plasmid import Plasmid
from strand import Strand
import ui


adenine = Plasmid('A')
thymine = Plasmid('T')
cytosine = Plasmid('C')
guanine = Plasmid('G')

sequence = ui.get_sequence()
strand = Strand(sequence)

original_strand = strand.sequence
complementary_strand = strand.modify_strand()

ui.print_strand(original_strand)
ui.print_strand(complementary_strand)

# original_strand = Strand(strand.get_original_strand())
# complementary_strand = Strand(strand.get_complementary_strand())

# restricted_original_strand = original_strand.cut_strand(original_strand.find_original_index())
# restricted_complementary_strand = complementary_strand.cut_strand(complementary_strand.find_complementary_index())
