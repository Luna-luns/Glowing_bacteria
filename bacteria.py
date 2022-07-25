import ui
import strand
from strand import Strand
from plasmid import Plasmid


adenine = Plasmid('A')
thymine = Plasmid('T')
cytosine = Plasmid('C')
guanine = Plasmid('G')

with open(ui.get_file_name().strip()) as file_name:
    lines = [line.strip() for line in file_name.readlines()]

original_plasmid_strand = Strand(lines[0])
plasmid_restriction_site = Strand(lines[1])

complementary_plasmid_restriction_site = Strand(plasmid_restriction_site.modify_strand())
complementary_plasmid_strand = Strand(original_plasmid_strand.modify_strand())
original_plasmid = Strand(original_plasmid_strand.
                          cut_strand(original_plasmid_strand.
                                     find_original_index(plasmid_restriction_site.sequence)))
complementary_plasmid = Strand(complementary_plasmid_strand.
                               cut_strand(complementary_plasmid_strand.
                                          find_complementary_index(complementary_plasmid_restriction_site.sequence)))
first_complimentary_plasmid = complementary_plasmid.get_first_strand()
second_complimentary_plasmid = complementary_plasmid.get_second_strand()

GFP_original_strand = Strand(lines[2])
GFP_restriction_sites = Strand(lines[3])

GFP_complementary_strand = Strand(GFP_original_strand.modify_strand())
GFP_first_part = Strand(GFP_restriction_sites.get_first_strand())
GFP_second_part = Strand(GFP_restriction_sites.get_second_strand())
GFP_complementary_first_part = Strand(GFP_first_part.modify_strand())
GFP_complementary_second_part = Strand(GFP_second_part.modify_strand())

cut_GFP_original_strand_beginning = Strand(GFP_original_strand.
                                           cut_strand(GFP_original_strand.
                                                      find_original_index(GFP_first_part.sequence)))
original_index_GFP_end = cut_GFP_original_strand_beginning.find_original_index(GFP_second_part.sequence)
cut_GFP_original_strand_end = Strand(cut_GFP_original_strand_beginning.cut_strand(original_index_GFP_end))
cut_GFP_complementary_strand_beginning = Strand(GFP_complementary_strand.
                                                cut_strand(GFP_complementary_strand.
                                                           find_complementary_index(GFP_complementary_first_part.
                                                                                    sequence)))
cut_GFP_complementary_strand_end = Strand(cut_GFP_complementary_strand_beginning.
                                          cut_strand(strand.find_complementary_index_gfp_end(original_index_GFP_end)))

origin_GFP = cut_GFP_original_strand_end.get_second_strand()
complementary_GFP = cut_GFP_complementary_strand_end.get_second_strand()

ligation_result = original_plasmid.\
    ligate_strands(origin_GFP, complementary_GFP, first_complimentary_plasmid, second_complimentary_plasmid)
ui.print_strand(ligation_result)
