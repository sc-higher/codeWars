# Sodoku Solution Validator
# https://www.codewars.com/kata/529bf0e9bdf7657179000008
#
# @author: Sean Connor

def validSolution(board):
  sudokuSet = set('123456789')
  # Check rows
  lrow = []
  for row in board:
    for val in row:
      lrow.append(str(val))
    srow = set(lrow)
    if srow != sudokuSet:
      return False
    lrow.clear()
    srow.clear()
  # Check columns
  for i in range(9):
    lcol = [str(row[i]) for row in board]
    scol = set(lcol)
    if scol != sudokuSet:
      return False
    lcol.clear()
    scol.clear()
  # Check inner squares
  lbox=[]
  m = 0
  while m<9:
    n = 0
    while n<9:
      for i in range(m,m+3):
        for j in range(n,n+3):
         lbox.append(str(board[i][j]))
      sbox=set(lbox)
      if sbox != sudokuSet:
        return False
      lbox.clear()
      sbox.clear()
      n+=3
    m+=3
  # If it gets to this point it is correct so...
  return True