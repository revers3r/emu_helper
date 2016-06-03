import vcpu_define
from convert_reg import *
from struct import *
from filtertable import *
from DB import *

def GetArgumentType(opcode):


def GetArgumentNum(opcode, array1, array2):
	if ord(opcode) not in array1:
		return 2
	elif ord(opcode) in array2:
		return 3
	else:
		return 1

a1_word, a2_word, a1_dword, a2_dword = 0, 0, 0, 0;
a1_byte, a2_byte = 0, 0;
insSet = Instruction()

class AsmEmulator:
	def Single_OpCode(self, data):
		arg_num = GetArgumentNum(data[0], filterlist, threeArgs)
		if arg_num == 2:
			typeArg1, Arg1_len = GetArgumentType()
	def Double_OpCode(self, data):
		## Not Prevention

	def Step(self, section, arg1, arg2, arg3 = None):

