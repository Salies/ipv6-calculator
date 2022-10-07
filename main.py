# 2001:0DB8:0000:0000:BEBA:0000:00C0:00CA

from re import compile
from sys import exit
from textwrap import wrap

def hex_to_bin(h):
    b = ""
    for c in h:
        b += str(bin(int(c, 16))[2:]).zfill(4)
    return b  

def bin_to_hex(b):
    h = ""
    for g in wrap(b, 4):
        h += str(hex(int(g, 2))[2:])
    return h

r = compile("(?:^|(?<=\s))(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))(?=\s|$)")
a = input()

if(not r.fullmatch(a)):
    print("ipv6 inválido")
    exit(1)

s = a.split(':')

if('' in s):
    if(s[-1] == ''):
        del s[-1]
    i = s.index('')
    del s[i]
    # Calcula o no. de grupos 0 que faltam e coloca no ip
    s = s[:i] + ((8 - len(s)) * ['0000']) + s[i:]

for i, grupo in enumerate(s):
    s[i] = grupo.zfill(4)

# String de grupos do ipv6 para números hexadecimais
#h = [hex(int(g, 16)) for g in s]
s = "".join(s)
# Descobrindo o grupo do meu barra
t_mask = 16
n_subnets = 10
bit_subnets = len(bin(n_subnets - 1)[2:])
# n = tamanho da máscara de saída
n = t_mask + bit_subnets
#gb = -(n // -16)
# Descobrindo o bit dentro do grupo
#b = n - (16 * (n // 16))
print("Divindindo a rede em", 2 ** bit_subnets, "redes /", n)
print(hex_to_bin(s))
print(bin_to_hex(hex_to_bin(s)))