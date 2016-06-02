########################################################
##                   Function's DB                    ##
########################################################

import string, itertools

def shift(lst, num):
	return itertools.islice(itertools.cycle(lst), num, num+len(lst))
class Instruction:
	def add(a1, a2):
		return (a1+a2) & 0xffffffff

	def push(a1, sp, data):
		lst = list(shift(a1, 1))
		lst[sp] = data
		return lst

	def pop(a1, sp, data):
		lst[sp] = 0
		lst = list(shift(a1, -1))
		return lst
