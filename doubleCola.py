# Double Cola
# https://www.codewars.com/kata/551dd1f424b7a4cdae0001f0
#
# @author: Sean Connor

def whoIsNext(names, r):
  i = r
  while i >= 6:
    i = (i-4)/2
  if i >= 1 and i < 2:
    return 'Sheldon'
  elif i >= 2 and i < 3:
    return 'Leonard'
  elif i >= 3 and i < 4:
    return 'Penny'
  elif i >= 4 and i < 5:
    return 'Rajesh'
  else: 
    return 'Howard'