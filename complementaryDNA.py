# Complementary DNA
# https://www.codewars.com/kata/554e4a2f232cdd87d9000038
#
# @author: Sean Connor

from string import maketrans

def DNA_strand(dna):
    intab = 'ATCGatcg'
    outtab = 'TAGCtagc'
    transtab = maketrans(intab,outtab)
    return dna.translate(transtab)