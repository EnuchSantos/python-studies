lista = []

while True:
    opcao = input(f'Selecione um opção\n[I]nserir [A]pagar [L]istar: ')

    if len(opcao) > 1 or opcao.isnumeric():
        print('Escolha apenas uma das opções destacadas!')
        continue

    if opcao in 'iI':
        nova_compra = input('Digite um item para inserir na lista: ')
        lista.append(nova_compra)
        print('Item adicionado a lista')
    elif opcao in 'aA':
        indice = input('Digite o indice da compra: ')
        if indice.isnumeric():
            indice = int(indice)
            del lista[indice]
            print('Item removido da lista!')
        else:
            print(
                'Você não digitou um número inteiro, por favor não coloque letras ou pontos flutuantes')
    elif opcao in 'lL':
        for indice, item in enumerate(lista):
            print(indice, item)
