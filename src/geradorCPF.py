"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

import random

nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0,9)) # gera inteiros aleatórios entre 0 e 9

multiplicador = 10
soma_nove_digitos = 0

for digito in nove_digitos:
    soma_nove_digitos += int(digito)*multiplicador
    multiplicador = multiplicador-1

#print(soma_nove_digitos)

previa_primeiro_digito = (soma_nove_digitos*10)%11
primeiro_digito = 0

if previa_primeiro_digito > 9:
    primeiro_digito = 0
else:
    primeiro_digito = previa_primeiro_digito

#print(primeiro_digito)

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

dez_digitos = nove_digitos + str(primeiro_digito)
#print(nove_digitos)

multiplicador_2 = 11
soma_dez_digitos = 0

for digito in dez_digitos:
    soma_dez_digitos += int(digito)*multiplicador_2
    multiplicador_2 = multiplicador_2-1

#print(soma_nove_digitos)

previa_segundo_digito = (soma_dez_digitos*10)%11
segundo_digito = 0

if previa_segundo_digito > 9:
    segundo_digito = 0
else:
    segundo_digito = previa_segundo_digito

#print(segundo_digito)

print(f'CPF gerado: {nove_digitos}{primeiro_digito}{segundo_digito}')