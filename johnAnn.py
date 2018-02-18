# John and Ann sign up for Codewars
# https://www.codewars.com/kata/57591ef494aba64d14000526
#
# @author: Sean Connor

def ann(n):
  a = [1]
  j = [0]
  i = 1
  while i < n:
    j.append(i-a[j[i-1]])
    a.append(i-j[a[i-1]])
    i += 1
  return a
  
def john(n):
  a = [1]
  j = [0]
  i = 1
  while i < n:
    j.append(i-a[j[i-1]])
    a.append(i-j[a[i-1]])
    i += 1
  return j
    
def sum_ann(n):
  return sum(ann(n))
    
def sum_john(n):
  return sum(john(n))