# WeIrD StRiNg CaSe
# https://www.codewars.com/kata/52b757663a95b11b3d00062d
#
# @author: Sean Connor

def to_weird_case(string):
  string_list = string.split()
  new_list = []
  for word in string_list:
    a = ''
    for i in range(len(word)):
      if i % 2 == 0:
        a = a + word[i].upper()
      else:
        a = a + word[i]
    word = a
    new_list.append(word)
  weird = ' '.join(new_list)
  print(weird)
  return weird