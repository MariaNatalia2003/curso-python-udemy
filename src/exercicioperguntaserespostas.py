# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
i = 0

for pergunta in perguntas:
    print(perguntas[i].get('Pergunta'))
    print("Indique o índice da resposta!!!")

    # enumerate pega o indice de 'Opções'
    for j, opcao in enumerate(perguntas[i].get('Opções')):
        print(f'{j}) ', opcao)

    resposta = int(input("Sua resposta: "))
    opcoes = pergunta['Opções']
    if opcoes[resposta] == perguntas[i].get('Resposta'):
        print("Você acertou! ✅")
        print()
        acertos += 1
    elif opcoes[resposta] != perguntas[i].get('Resposta'):
        print("Você errou! ❌")
        print()
    i+=1

if acertos > 0:
    print(f'Parabéns! Você acertou {acertos} questões 🥳')
else:
    print("Que pena, você não acertou nenhuma questão 🫤")