import struct, time
import operator

p = lambda x: struct.pack("<L", x)
up = lambda x: struct.unpack("<L", x)[0]

register_class = {'eax':0, 'ebx':1, 'ecx':2, 'edx':3,
					'ebp':4, 'esp':5, 'esi':6, 'edi':7, 'eip':8}
OK = 0;
dataStructure = [0x0] * 9;
base, stackBase = 0x00000000, 0xbf000000;
def is_null(value):
	if value == 0:
		return True;
	return False;

class FileClass:
	def ImageBase(self, file_name):
		fp = open(file_name, 'rb').read()
		return up(fp[0x18:0x18+4])

class DefineStructure:
	#################################################################
	## 1) EAX            2) EBX            3) ECX           4) EDX ##
	## 5) EBP            6) ESP            7) ESI           8) EDI ##
	## 9) EIP                                                      ##
	#################################################################
	def push_register(self, reg, value=0x0):
		dataStructure[reg] = value
		return OK;

	def reset_register(self):
		for i in range(9):
			dataStructure[i] = 0;
		return OK;

	def print_register(self, reg):
		print "[*] %s : 0x%08x" % (reg.upper(), dataStructure[register_class[reg]])

	def get_register(self, reg):
		return dataStructure[register_class[reg]]