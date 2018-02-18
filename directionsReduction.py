# Directions Reduction
# https://www.codewars.com/kata/550f22f4d758534c1100025a
#
# @author: Sean Connor

def dirReduc(arr):
  a = []
  for i in arr:
    if i == 'NORTH':
      a.append(1)
    elif i == 'SOUTH':
      a.append(-1)
    elif i == 'EAST':
      a.append(2)
    else:
      a.append(-2)
  i = 1
  while i < len(a):
    if len(a)==0:
      return []
    elif len(a)==1:
      return a
    elif a[i-1]+a[i]==0:
      del a[i]
      del a[i-1]
      del arr[i]
      del arr[i-1]
      i = 1
    else:
      i += 1
  return arr