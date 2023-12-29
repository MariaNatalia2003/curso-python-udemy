'''
Exercícios

Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro
'''

def operacao(multiplicador):
    def resultado(num):
        return multiplicador*num
    return resultado

duplicar = operacao(2)
triplicar = operacao(3)
quadruplicar = operacao(4)

try:
    numero = float(input("Digite um número: "))
except:
    print("Isso não é um número!")
    numero = float(input("Digite um número: "))

print(f'Dobro: {duplicar(numero)}')
print(f'Triplo: {triplicar(numero)}')
print(f'Quadruplo: {quadruplicar(numero)}')