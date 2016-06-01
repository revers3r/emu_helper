import vcpu_define

low_byte, high_byte, word, dword = 0, 0, 0, 0;
RegStruct = [];
class ConvertType:
	def __init__(self, array):
		RegStruct = array;

	def _ConvertByte(self, type, value):
		if type == 'high':
			high_byte = (value << 8) & 0x0000ff00
			return high_byte
		elif type == 'low':
			low_byte = (value & 0x000000ff)
			return low_byte
