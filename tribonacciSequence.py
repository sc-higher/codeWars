# Tribonacci Sequence
# https://www.codewars.com/kata/556deca17c58da83c00002db
#
# @author: Sean Connor

def tribonacci(sig, n):
    if n == 0:
        return []
    if n == 1:
        return [sig[0]]
    if n == 2:
        return [sig[0], sig[1]]
    if n == 3:
        return [sig[0], sig[1], sig[2]]
    if n > 3:
        for i in range(n-3):
            sig.append(sig[i]+sig[i+1]+sig[i+2])
        return sig