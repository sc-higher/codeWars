# ROT13
# https://www.codewars.com/kata/52223df9e8f98c7aa7000062
#
# @author: Sean Connor

def rot13(message):
  
  alphal={'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t',
  'h':'u','i':'v','j':'w','k':'x','l':'y','m':'z','n':'a','o':'b',
  'p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j',
  'x':'k','y':'l','z':'m'}

  alphac={'A':'N','B':'O','C':'P','D':'Q','E':'R','F':'S','G':'T',
  'H':'U','I':'V','J':'W','K':'X','L':'Y','M':'Z','N':'A','O':'B',
  'P':'C','Q':'D','R':'E','S':'F','T':'G','U':'H','V':'I','W':'J',
  'X':'K','Y':'L','Z':'M'}
  
  trans=''
  
  for c in message:
    if c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
      trans=trans+c
    elif c in 'abcdefghijklmnopqrstuvwxyz':
      trans=trans+alphal[c]
    else:
      trans=trans+alphac[c]
  
  return(trans)