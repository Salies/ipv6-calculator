# Redes de Computadores II - FCT-UNESP
# Atividade 1
# Daniel Henrique Serezane Pereira

from re import compile
from sys import exit
from textwrap import wrap

# Fomrata um número hexadecimal 128 bits em um ipv6
def format_ipv6(ip):
    return ':'.join(wrap(ip, 4)).upper()

# Verifica se uma string representa um número
def verifica_numero(string, err):
    try:
        n = int(string)
        return n
    except ValueError:
        print(err)
        exit(1)

# Imprime as redes rightmost e leftmost
def print_redes(listas, cidr):
    print()
    for lista in listas:
        print(lista['nome'])
        for rede in lista['redes']:
            print(rede + '/' + str(cidr))
        print()

# Expressão regular para validar um endereço IPV6
r = compile("(?:^|(?<=\s))(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))(?=\s|$)")
a = input("Insira um endereço IPV6: ")

# Validando a entrada
if(not r.fullmatch(a)):
    print("IPV6 inválido.")
    exit(1)

# Tratando abreviações do ipv6
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
s = "".join(s)
# Descobrindo o grupo do meu barra
t_mask = input("Escolha uma máscara (0-128): /")
t_mask = verifica_numero(t_mask, "Máscara inválida.")
n_subnets = input("Alocar quantas redes? ")
n_subnets = verifica_numero(n_subnets, "Número inválido.")
bit_subnets = len(bin(n_subnets - 1)[2:])
# n = tamanho da máscara de saída
n = t_mask + bit_subnets
print("\nAlocando", 2 ** bit_subnets, "redes", ("/" + str(n) + "."))
# Transformado o hexadecimal em número e aplicando o CIDR
s_no = int(s, 16) & (0xffffffffffffffffffffffffffffffff << (128 - t_mask))
# Fazendo o RightMost e o LeftMost
# e armazenando as redes resultantes
c = "0" * (128 - n)
offset = lambda a : int(a + c, 2)
to_ip = lambda b : format_ipv6(hex(s_no | offset(b))[2:])
r_res = []
l_res = []
for i in range(2 ** bit_subnets):
    r = format(i, f'0{bit_subnets}b')
    r_res.append(to_ip(r))
    l_res.append(to_ip(r[::-1]))

print_redes(
[
    {
        'nome': "Rightmost",
        'redes': r_res
    },
    {
        'nome': "Leftmost",
        'redes': l_res
    }
],
n
)