palavrasecreta = 'algoritmo'
tentativas = 0
letras_acertadas = ''

while True:
    letra = input('Digite uma letra: ')
    tentativas += 1
    if(len(letra) > 1):
        print('Digite apenas uma letra.')
        continue

    if letra in palavrasecreta:
        letras_acertadas += letra

    palavraformatada = ''

    for letra_secreta in palavrasecreta:
        if letra_secreta in letras_acertadas:
            palavraformatada += letra_secreta
        else:
            palavraformatada += '*'

    print(f'Palavra formatada: {palavraformatada}')

    if(palavraformatada == palavrasecreta):
        break

print("Você adivinhou a palavra secreta!!!")
print('Plavara secreta: ', palavrasecreta)
print(f'Tentativas: {tentativas}')