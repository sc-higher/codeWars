# Calculate average
# https://www.codewars.com/kata/57a2013acf1fa5bfc4000921
#
# @author: Sean Connor

def find_average(array):
    if array == []:
        return 0
    else:
        return sum(array)/len(array)