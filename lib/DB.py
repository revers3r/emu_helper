########################################################
##                   Function's DB                    ##
########################################################

import string, itertools

def shift(lst, num):
	return itertools.islice(itertools.cycle(lst), num, num+len(lst))

class Instruction:
	def _add(self, a1, a2):
		result = a1 + a2
		carry_flag = 0
		if result >= 0x100000000:
			carry_flag = 1
			return carry_flag, (result & 0xffffffff)
		return carry_flag, (result & 0xffffffff)

	def _push(self, a1, sp, data):
		lst = a1
		lst.insert(sp, data)
		return lst

	def _pop(self, a1, sp, data):
		lst2 = lst
		del lst2[sp]
		return lst2

	def _or(self, a1, a2):
		return (a1 | a2) & 0xffffffff

	def _adc(self, a1, a2, cflag):
		result = a1 + a2 + cflag
		carry_flag = 0
		if result >= 0x100000000:
			carry_flag = 1
			return carry_flag, (result & 0xffffffff)
		return carry_flag, (result & 0xffffffff)

	def _sbb(self, a1, a2, cflag):
		result = a1 - (a2 + cflag)
		carry_flag = 0
		if result < 0:
			carry_flag = 1
			return carry_flag, (result & 0xffffffff)
		return carry_flag, (result & 0xffffffff)

	def _and(self, a1, a2):
		return (a1 & a2);

	def _sub(self, a1, a2):
		result = a1 - a2;
		carry_flag = 0;
		if result < 0:
			carry_flag = 1
			return carry_flag, (result & 0xffffffff)
		return carry_flag, (result & 0xffffffff)

	def _xor(self, a1, a2):
		result = a1 ^ a2
		zero_flag = 0
		if result == 0:
			zero_flag = 1
			return zero_flag, (result & 0xffffffff)
		return zero_flag, (result & 0xffffffff)

	def _cmp(self, a1, a2):
		zero_flag = 0
		if a1 == a2:
			zero_flag = 1
			return 0, zero_flag
		else:
			return 1, zero_flag

	