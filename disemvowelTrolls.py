# Disemvowel Trolls
# https://www.codewars.com/kata/52fba66badcd10859f00097e
#
# @author: Sean Connor

def disemvowel(string):
    return ''.join(a for a in string if a not in 'aeiouAEIOU')