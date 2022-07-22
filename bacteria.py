from plasmid import Plasmid
from strand import Strand
import ui


adenine = Plasmid('A')
thymine = Plasmid('T')
cytosine = Plasmid('C')
guanine = Plasmid('G')
sequence = ui.get_sequence()
strand = Strand(sequence)
ui.print_strand(strand.modify_strand())
