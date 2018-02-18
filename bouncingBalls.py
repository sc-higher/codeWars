# Bouncing Balls
# https://www.codewars.com/kata/5544c7a5cb454edb3c000047
#
# @author: Sean Connor

def bouncingBall(h, bounce, window):
  if h>0 and h>window and 0<bounce<1:
    i = 0
    while h > window:
      h = h * bounce
      i += 2
    return i-1
  else:
    return -1