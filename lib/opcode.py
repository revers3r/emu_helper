
# Instruction OpCode Table
add_eb_gb = 0x00
add_ev_gv = 0x01
add_gb_eb = 0x02
add_gv_ev = 0x03
add_al_lb = 0x04
add_eax_lv = 0x05

push_es = 0x06
pop_es = 0x07

or_eb_gb = 0x08
or_ev_gv = 0x09
or_gb_eb = 0x0a
or_gv_ev = 0x0b
or_al_lb = 0x0c
or_eax_lv = 0x0d

push_cs = 0x0e
# TWOBYTE 0x0f

adc_eb_gb = 0x10
adc_ev_gv = 0x11
adc_gb_eb = 0x12
adc_gv_ev = 0x13
adc_al_lb = 0x14
adc_eax_lv = 0x15

push_ss = 0x16
pop_ss = 0x17

sbb_eb_gb = 0x18
sbb_ev_gv = 0x19
sbb_gb_eb = 0x1a
sbb_gv_ev = 0x1b
sbb_al_lb = 0x1c
sbb_eax_lv = 0x1d

push_ds = 0x1e
pop_ds = 0x1f

and_eb_gb = 0x20
and_ev_gv = 0x21
and_gb_eb = 0x22
and_gv_ev = 0x23
and_al_lb = 0x24
and_eax_lv = 0x25

es_segment = 0x26
daa = 0x27

sub_eb_gb = 0x28
sub_ev_gv = 0x29
sub_gb_eb = 0x2a
sub_gv_ev = 0x2b
sub_al_lb = 0x2c
sub_eax_lv = 0x2d

cs_segment = 0x2e
das = 0x2f

xor_eb_gb = 0x30
xor_ev_gv = 0x31
xor_gb_eb = 0x32
xor_gv_ev = 0x33
xor_al_lv = 0x34
xor_eax_lv = 0x35

ss_segment = 0x36
aaa = 0x37

cmp_eb_gb = 0x38
cmp_ev_gv = 0x39
cmp_gb_eb = 0x3a
cmp_gv_ev = 0x3b
cmp_al_lb = 0x3c
cmp_eax_lv = 0x3d

ds_segment = 0x3e
aas = 0x3f

inc_eax = 0x40
inc_ecx = 0x41
inc_edx = 0x42
inc_ebx = 0x43
inc_esp = 0x44
inc_ebp = 0x45
inc_esi = 0x46
inc_edi = 0x47

dec_eax = 0x48
dec_ecx = 0x49
dec_edx = 0x4a
dec_ebx = 0x4b
dec_esp = 0x4c
dec_ebp = 0x4d
dec_esi = 0x4e
dec_edi = 0x4f

push_eax = 0x50
push_ecx = 0x51
push_edx = 0x52
push_ebx = 0x53
push_esp = 0x54
push_ebp = 0x55
push_esi = 0x56
push_edi = 0x57

pop_eax = 0x58
pop_ecx = 0x59
pop_edx = 0x5a
pop_ebx = 0x5b
pop_esp = 0x5c
pop_ebp = 0x5d
pop_esi = 0x5e
pop_edi = 0x5f

pusha = 0x60
popa = 0x61

bound_gv_ma = 0x62

arpl_ew_gw = 0x63

fs_segment = 0x64
gs_segment = 0x65

opsize_tag = 0x66
adsize_tag = 0x67

push_lv = 0x68
imul_gv_ev_lv = 0x69
push_lv = 0x6a
imul_gv_ev_lb = 0x6b

insb_yb_dx = 0x6c
insw_yz_dx = 0x6d
outsb_dx_xb = 0x6e
outsw_dx_xv = 0x6f

jo = 0x70
jno = 0x71
jb = 0x72
jnb = 0x73
jz = 0x74
jnz = 0x75
jbe = 0x76
ja = 0x77
js = 0x78
jns = 0x79
jp = 0x7a
jnp = 0x7b
jl = 0x7c
jnl = 0x7d
jle = 0x7e
jnle = 0x7f

add_eb_lb = 0x80
add_ev_lv = 0x81

sub_eb_lb = 0x82
sub_ev_lb = 0x83

test_eb_gb = 0x84
test_ev_gv = 0x85

xchg_eb_gb = 0x86
xchg_ev_gv = 0x87

mov_eb_gb = 0x88
mov_ev_gv = 0x89
mov_gb_eb = 0x8a
mov_gv_ev = 0x8b
mov_ew_sw = 0x8c

lea_gv_m = 0x8d

mov_sw_ew = 0x8e

pop_ev = 0x8f
nop = 0x90

xchg_eax_ecx = 0x91
xchg_eax_edx = 0x92
xchg_eax_ebx = 0x93
xchg_eax_esp = 0x94
xchg_eax_ebp = 0x95
xchg_eax_esi = 0x96
xchg_eax_edi = 0x97

cbw = 0x98
cwd = 0x99

call_ap = 0x9a

wait = 0x9b
pushf_fv = 0x9c
popf_fv = 0x9d

sahf = 0x9e
lahf = 0x9f

mov_al_ob = 0xa0
mov_eax_ov = 0xa1
mov_ob_al = 0xa2
mov_ov_eax = 0xa3

movsb_xb_yb = 0xa4
movsw_xv_yv = 0xa5
cmpsb_xb_yb = 0xa6
cmpsw_xv_yv = 0xa7

test_al_lb = 0xa8
test_eax_lv = 0xa9

stosb_yb_al = 0xaa
stosw_yv_eax = 0xab
lodsb_al_xb = 0xac
lodsw_eax_xv = 0xad
scasb_al_yb = 0xae
scasw_eax_yv = 0xaf

mov_al_lb = 0xb0
mov_cl_lb = 0xb1
mov_dl_lb = 0xb2
mov_bl_lb = 0xb3
mov_ah_lb = 0xb4
mov_ch_lb = 0xb5
mov_dh_lb = 0xb6
mov_bh_lb = 0xb7
mov_eax_lv = 0xb8
mov_ecx_lv = 0xb9
mov_edx_lv = 0xba
mov_ebx_lv = 0xbb
mov_esp_lv = 0xbc
mov_ebp_lv = 0xbd
mov_esi_lv = 0xbe
mov_edi_lv = 0xbf

w_eb_lb = 0xc0
w_ev_lb = 0xc1

retn_lw = 0xc2
retn = 0xc3
les_gv_mp = 0xc4
lds_gv_mp = 0xc5

mov_eb_lb = 0xc6
mov_ev_lv = 0xc7

enter_lw_lb = 0xc8
leave = 0xc9
retf_lw = 0xca
retf = 0xcb

int3 = 0xcc
int_lb = 0xcd
into = 0xce
iret = 0xcf

w_eb_1 = 0xd0
w_ev_1 = 0xd1
w_eb_cl = 0xd2
w_ev_cl = 0xd3

aam_lb = 0xd4
aad_lb = 0xd5

salc = 0xd6
xlat = 0xd7

esc_0 = 0xd8
esc_1 = 0xd9
esc_2 = 0xda
esc_3 = 0xdb
esc_4 = 0xdc
esc_5 = 0xdd
esc_6 = 0xde
esc_7 = 0xde


loopnz_jb = 0xe0
loopz_jb = 0xe1
loop_jb = 0xe2
jcxz_jb = 0xe3
in_al_lb = 0xe4
in_eax_lb = 0xe5
out_lb_al = 0xe6
out_lb_eax = 0xe7
call_jz = 0xe8
jmp_jz = 0xe9
jmp_ap = 0xea
jmp_jb = 0xeb

in_al_dx = 0xec
in_eax_dx = 0xed

out_dx_al = 0xee
out_dx_eax = 0xef

lock_segment = 0xf0
int1 = 0xf1

repne = 0xf2
rep = 0xf3

hlt = 0xf4
cmc = 0xf5

w3_eb = 0xf6
w3_ev = 0xf7

clc = 0xf8
stc = 0xf9
cli = 0xfa
sti = 0xfb
cld = 0xfc
std = 0xfd

w4_inc_dec = 0xfe
w5_inc_dec = 0xff


opcode_list = {add_eb_gb:0x0, add_ev_gv:0x1, add_gb_eb:0x2, 
				add_gv_ev:0x3, add_al_lb:0x4, add_eax_lv:0x5,
				push_es:0x6, pop_es:0x7, or_eb_gb:0x08,
or_ev_gv:0x09,
or_gb_eb:0x0a,
or_gv_ev:0x0b,
or_al_lb:0x0c,
or_eax_lv:0x0d,
push_cs:0x0e,
adc_eb_gb:0x10,
adc_ev_gv:0x11,
adc_gb_eb:0x12,
adc_gv_ev:0x13,
adc_al_lb:0x14,
adc_eax_lv:0x15,
push_ss:0x16,
pop_ss:0x17,
sbb_eb_gb:0x18,
sbb_ev_gv:0x19,
sbb_gb_eb:0x1a,
sbb_gv_ev:0x1b,
sbb_al_lb:0x1c,
sbb_eax_lv:0x1d,
push_ds:0x1e,
pop_ds:0x1f,
and_eb_gb:0x20,
and_ev_gv:0x21,
and_gb_eb:0x22,
and_gv_ev:0x23,
and_al_lb:0x24,
and_eax_lv:0x25,
es_segment:0x26,
daa:0x27,
sub_eb_gb:0x28,
sub_ev_gv:0x29,
sub_gb_eb:0x2a,
sub_gv_ev:0x2b,
sub_al_lb:0x2c,
sub_eax_lv:0x2d,
cs_segment:0x2e,
das:0x2f,
xor_eb_gb:0x30,
xor_ev_gv:0x31,
xor_gb_eb:0x32,
xor_gv_ev:0x33,
xor_al_lv:0x34,
xor_eax_lv:0x35,
ss_segment:0x36,
aaa:0x37,
cmp_eb_gb:0x38,
cmp_ev_gv:0x39,
cmp_gb_eb:0x3a,
cmp_gv_ev:0x3b,
cmp_al_lb:0x3c,
cmp_eax_lv:0x3d,
ds_segment:0x3e,
aas:0x3f,
inc_eax:0x40,
inc_ecx:0x41,
inc_edx:0x42,
inc_ebx:0x43,
inc_esp:0x44,
inc_ebp:0x45,
inc_esi:0x46,
inc_edi:0x47,
dec_eax:0x48,
dec_ecx:0x49,
dec_edx:0x4a,
dec_ebx:0x4b,
dec_esp:0x4c,
dec_ebp:0x4d,
dec_esi:0x4e,
dec_edi:0x4f,
push_eax:0x50,
push_ecx:0x51,
push_edx:0x52,
push_ebx:0x53,
push_esp:0x54,
push_ebp:0x55,
push_esi:0x56,
push_edi:0x57,
pop_eax:0x58,
pop_ecx:0x59,
pop_edx:0x5a,
pop_ebx:0x5b,
pop_esp:0x5c,
pop_ebp:0x5d,
pop_esi:0x5e,
pop_edi:0x5f,
pusha:0x60,
popa:0x61,
bound_gv_ma:0x62,
arpl_ew_gw:0x63,
fs_segment:0x64,
gs_segment:0x65,
opsize_tag:0x66,
adsize_tag:0x67,
push_lv:0x68,
imul_gv_ev_lv:0x69,
push_lv:0x6a,
imul_gv_ev_lb:0x6b,
insb_yb_dx:0x6c,
insw_yz_dx:0x6d,
outsb_dx_xb:0x6e,
outsw_dx_xv:0x6f,
jo:0x70,
jno:0x71,
jb:0x72,
jnb:0x73,
jz:0x74,
jnz:0x75,
jbe:0x76,
ja:0x77,
js:0x78,
jns:0x79,
jp:0x7a,
jnp:0x7b,
jl:0x7c,
jnl:0x7d,
jle:0x7e,
jnle:0x7f,
add_eb_lb:0x80,
add_ev_lv:0x81,
sub_eb_lb:0x82,
sub_ev_lb:0x83,
test_eb_gb:0x84,
test_ev_gv:0x85,
xchg_eb_gb:0x86,
xchg_ev_gv:0x87,
mov_eb_gb:0x88,
mov_ev_gv:0x89,
mov_gb_eb:0x8a,
mov_gv_ev:0x8b,
mov_ew_sw:0x8c,
lea_gv_m:0x8d,
mov_sw_ew:0x8e,
pop_ev:0x8f,
nop:0x90,
xchg_eax_ecx:0x91,
xchg_eax_edx:0x92,
xchg_eax_ebx:0x93,
xchg_eax_esp:0x94,
xchg_eax_ebp:0x95,
xchg_eax_esi:0x96,
xchg_eax_edi:0x97,
cbw:0x98,
cwd:0x99,
call_ap:0x9a,
wait:0x9b,
pushf_fv:0x9c,
popf_fv:0x9d,
sahf:0x9e,
lahf:0x9f,
mov_al_ob:0xa0,
mov_eax_ov:0xa1,
mov_ob_al:0xa2,
mov_ov_eax:0xa3,
movsb_xb_yb:0xa4,
movsw_xv_yv:0xa5,
cmpsb_xb_yb:0xa6,
cmpsw_xv_yv:0xa7,
test_al_lb:0xa8,
test_eax_lv:0xa9,
stosb_yb_al:0xaa,
stosw_yv_eax:0xab,
lodsb_al_xb:0xac,
lodsw_eax_xv:0xad,
scasb_al_yb:0xae,
scasw_eax_yv:0xaf,
mov_al_lb:0xb0,
mov_cl_lb:0xb1,
mov_dl_lb:0xb2,
mov_bl_lb:0xb3,
mov_ah_lb:0xb4,
mov_ch_lb:0xb5,
mov_dh_lb:0xb6,
mov_bh_lb:0xb7,
mov_eax_lv:0xb8,
mov_ecx_lv:0xb9,
mov_edx_lv:0xba,
mov_ebx_lv:0xbb,
mov_esp_lv:0xbc,
mov_ebp_lv:0xbd,
mov_esi_lv:0xbe,
mov_edi_lv:0xbf,
w_eb_lb:0xc0,
w_ev_lb:0xc1,
retn_lw:0xc2,
retn:0xc3,
les_gv_mp:0xc4,
lds_gv_mp:0xc5,
mov_eb_lb:0xc6,
mov_ev_lv:0xc7,
enter_lw_lb:0xc8,
leave:0xc9,
retf_lw:0xca,
retf:0xcb,
int3:0xcc,
int_lb:0xcd,
into:0xce,
iret:0xcf,
w_eb_1:0xd0,
w_ev_1:0xd1,
w_eb_cl:0xd2,
w_ev_cl:0xd3,
aam_lb:0xd4,
aad_lb:0xd5,
salc:0xd6,
xlat:0xd7,
esc_0:0xd8,
esc_1:0xd9,
esc_2:0xda,
esc_3:0xdb,
esc_4:0xdc,
esc_5:0xdd,
esc_6:0xde,
esc_7:0xde,
loopnz_jb:0xe0,
loopz_jb:0xe1,
loop_jb:0xe2,
jcxz_jb:0xe3,
in_al_lb:0xe4,
in_eax_lb:0xe5,
out_lb_al:0xe6,
out_lb_eax:0xe7,
call_jz:0xe8,
jmp_jz:0xe9,
jmp_ap:0xea,
jmp_jb:0xeb,
in_al_dx:0xec,
in_eax_dx:0xed,
out_dx_al:0xee,
out_dx_eax:0xef,
lock_segment:0xf0,
int1:0xf1,
repne:0xf2,
rep:0xf3,
hlt:0xf4,
cmc:0xf5,
w3_eb:0xf6,
w3_ev:0xf7,
clc:0xf8,
stc:0xf9,
cli:0xfa,
sti:0xfb,
cld:0xfc,
std:0xfd,
w4_inc_dec:0xfe,
w5_inc_dec:0xff}