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

	def _inc(self, a1):
		result = a1 + 1;
		carry_flag = 0
		zero_flag = 0
		if result >= 0x100000000:
			carry_flag = 1
		elif result == 0:
			zero_flag = 1
		return zero_flag, carry_flag, (result & 0xffffffff)

	def _dec(self, a1):
		result = a1 - 1;
		carry_flag, zero_flag = 0, 0
		if result < 0x0:
			carry_flag = 1
		elif result == 0x0:
			zero_flag = 1
		return zero_flag, carry_flag, (result & 0xffffffff)

	def _imul(self, a1, a2, a3):
		result = a2 * a3;
		carry_flag, zero_flag = 0, 0
		if result >= 0x100000000:
			carry_flag = 1
			return carry_flag, zero_flag, (result & 0xffffffff)
		elif result == 0x0:
			zero_flag = 1

		return carry_flag, zero_flag, (result & 0xffffffff)

	def _mov(self, a1, a2):
		return a2;

	def _nop(self):
		return;

	def _xchg(self, a1, a2):
		return a2, a1;

	
