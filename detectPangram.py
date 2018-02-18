# Detect Pangram
# https://www.codewars.com/kata/545cedaa9943f7fe7b000048
#
# @author: Sean Connor

def is_pangram(s):
  s = s.translate({ord(c): None for c in ' !@#$%^&*()_+-=[]\{}|;:,./<>?`~"'})
  s = s.lower()
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  for letter in s:
    if letter in alphabet:
      alphabet = alphabet.translate({ord(c): None for c in letter})
  if alphabet == '':
    return True
  else: 
    return False