# from plasmid import Plasmid
from strand import Strand
import ui


# adenine = Plasmid('A')
# thymine = Plasmid('T')
# cytosine = Plasmid('C')
# guanine = Plasmid('G')
#
# _strand = Strand(ui.get_sequence())  # CCTGCAGGTCGACTCTAGAGGATCCCCGGGTACCTAGAATTGCACGCA
# complementary_stand = Strand(_strand.modify_strand())  # GGACGTCCAGCTGAGATCTCCTAGGGGCCCATGGATCTTAACGTGCGT
#
# restriction_sites = Strand(ui.get_sequence())  # CTGCAG TTGCAC
# first_part = restriction_sites.get_first_strand()  # CTGCAG
# second_part = restriction_sites.get_second_strand()  # TTGCAC
#
# complementary_first_part = Strand(first_part)
# complementary_first_part_GFP = complementary_first_part.modify_strand()  # GACGTC
#
# complementary_second_part = Strand(second_part)
# complementary_second_part_GFP = complementary_second_part.modify_strand()  # AACGTG
#
# cut_original_strand_beginning = Strand(_strand.cut_strand(_strand.find_original_index(first_part)))
# cut_complementary_strand_beginning = Strand(complementary_stand.cut_strand(complementary_stand.find_complementary_index(complementary_first_part_GFP)))
#
# cut_original_strand_end = Strand(cut_original_strand_beginning.cut_strand(cut_original_strand_beginning.find_original_index(second_part)))
# cut_complementary_strand_end = Strand(cut_complementary_strand_beginning.cut_strand(cut_complementary_strand_beginning.find_complementary_index(complementary_second_part_GFP)))
#
# origin_GFP = cut_original_strand_end.get_second_strand()
# complementary_GFP = cut_complementary_strand_end.get_second_strand()
#
# ui.print_strand(origin_GFP)
# ui.print_strand(complementary_GFP)

with open(ui.get_file_name().strip()) as file_name:
    lines = file_name.readlines()

first_line = lines[0].split()  # plasmid
second_line = Strand(lines[1])  # GFP
ligation_result = second_line.ligate_strands(first_line)
ui.print_strand(ligation_result)
