"""
Faça uma lista de compras com lista.
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""

lista_compras = []

while True:
    print('Selecione uma opção:\n')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ')

    if(opcao.lower() == 'i'):
        coisa = input("Item: ")
        lista_compras.append(coisa)
    elif(opcao.lower()=='a'):
        indice_str = input('Selecione o indice a apagar: ')
        try:
            indice = int(indice_str)
            del lista_compras[indice]
        except:
            print('Não foi possível apagar esse índice.')
    elif(opcao.lower()=='l'):
        if len(lista_compras)==0:
            print('Não há itens a serem listados')

        for i, item in enumerate(lista_compras):
            print(i, item)
    elif(opcao.lower()=='s'):
        break
    else:
        print('Digite uma opção válida.')