from vcpu_define import *
from convert_reg import *
from emulator import *

def_vcpu = DefineStructure();
registers = def_vcpu.reset_register()
fileClass = FileClass()
imagebase = fileClass.ImageBase('reverseme')

def_vcpu.push_register(register_class['esp'], stackBase)
def_vcpu.push_register(register_class['eip'], imagebase)

def_vcpu.print_register('eip')
def_vcpu.print_register('esp')

convReg = ConvertType(dataStructure)
low_eip = convReg._ConvertByte('low', def_vcpu.get_register('eip'))
high_eip = convReg._ConvertByte('high', def_vcpu.get_register('eip'))

############################################
##                  Test                  ##
############################################
print "0x%x" % low_eip
print "0x%x" % high_eip
