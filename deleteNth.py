# Delete occurrences of an element if it occurs more than n times
# https://www.codewars.com/kata/554ca54ffa7d91b236000023
#
# @author: Sean Connor

def delete_nth(order,max_e):
  order.reverse()
  i = 0
  while i < len(order):
    for j in order:
      if order.count(j) > max_e:
        order.remove(j)
        i = 0
      else:
        i += 1
  order.reverse()
  return order