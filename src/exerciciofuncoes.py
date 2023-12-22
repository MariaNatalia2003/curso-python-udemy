# Exercícios com funções

'''
1. Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor
da variável.

2. Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.
'''

def multiplicacao(*args):
    total = 1

    try:
        for numero in args:
            total *= float(numero)

        return total
    except:
        return print("Algum dos argumentos não é um número.")

    
def paridade(num):

    try:
        num_float = float(num)
    except:
        return print("Isso não é um número.")
    
    if (num_float%2) == 0:
        return "O número é par."
    return "O número é ímpar."

res_multiplicacao = multiplicacao(1, 2, 3)
print(res_multiplicacao)

res_multiplicacao1 = multiplicacao(10, 10, 10)
print(res_multiplicacao1)

res_multiplicacao2 = multiplicacao(1, "e")

par1 = paridade(34)
print(par1)

impar1 = paridade(27)
print(impar1)

nada = paridade("u")

res_multiplicacao3 = multiplicacao(1.5, 2.3, 5.6)
print(res_multiplicacao3)