# Importação para apenas colocar um intervalo entre os prints
import time

# Criação de listas dos sabores e bebida com seus respectivos preços
sabores = [
    ['Calabresa', 10],
    ['Mussarela', 15],
    ['Marguerita', 20]
]

bebidas = [
    ['Suco', 10],
    ['Refrigerante', 15]
]

print('Olá, Bem Vindo!')


# Função para o menu de opções retornando a opção escolhida pelo usuário
def menu():
    print('-' * 15 + '\nEscolha uma opção:\n[1] - Sabores\n[2] - Bebidas\n[3] - Confirmar Dados\n' + '-' * 15)
    opcao = int(input('Digite uma opção acima: '))
    return opcao


# Funções para escolher o sabor da pizza e a bebida, se o valor digitado estiver incorreto o programa solicitará para
# tentar novamente
def escolher_sabor():
    print('-' * 15 + '\nEscolha um sabor:')
    for sabor in sabores:
        print(f'{sabor[0]} -R${sabor[1]}\n' + '-' * 15)
    sabor_escolhido = input('Digite o nome do sabor escolhido: ').capitalize()
    while not any(sabor_escolhido == sabor[0] for sabor in sabores):
        sabor_escolhido = input('Sabor inválido, tente novamente: ').capitalize()
    preco_sabor = next(sabor[1] for sabor in sabores if sabor[0] == sabor_escolhido)

    return sabor_escolhido, preco_sabor


def escolher_bebida():
    print('-' * 15 + '\nEscolha uma bebida:')
    for bebida in bebidas:
        print(f'{bebida[0]} - R${bebida[1]}\n' + '-' * 15)
    bebida_escolhida = input('Digite uma bebida acima: ').capitalize()
    while not any(bebida_escolhida == bebida[0] for bebida in bebidas):
        bebida_escolhida = input('Bebida inválida, tente novamente:')
    preco_bebida = next(bebida[1] for bebida in bebidas if bebida[0] == bebida_escolhida)

    return bebida_escolhida, preco_bebida


# Função para confirmar o pedido, mais a frente se o cliente quiser refazer o pedido ou o programa estiver errado,
# poderá fazer denovo
def confirmar_dados(sabor_escolhido, preco_sabor, bebida_escolhida, preco_bebida):
    print(f'Sabor escolhido: {sabor_escolhido}\nBebida escolhida:  {bebida_escolhida}')


# Função para o usuário escolher a forma de pagamento
def pagamento():
    formas = {
        '1': 'Cartão de Crédito',
        '2': 'Cartão de Débito',
        '3': 'Pix',
        '4': 'Dinheiro'
    }
    pag = input('Escolha uma forma de pagamento:\n[1] - Cartão Crédito\n[2] - Cartão Débito\n[3] - Pix\n'
                '[4] - Dinheiro\n')
    while pag not in formas:
        pag = input('Opção Inválida, tente novamente')
    print(f'Forma de pagamento - {formas[pag]}')


# Main - Usando o while para sempre que as opções sejam verdadeiras, continuará retornando o menu de opções,
# até o usuário quiser confirmar o pedido
while True:
    opcao = menu()

    if opcao == 1:
        sabor_escolhido, preco_sabor = escolher_sabor()
    elif opcao == 2:
        bebida_escolhida, preco_bebida = escolher_bebida()
    elif opcao == 3:
        confirmar_dados(sabor_escolhido, preco_sabor, bebida_escolhida, preco_bebida)
        nome = str(input('-' * 15 + '\nInforme seu nome: '))
        endereco = str(input('-' * 15 + '\nInforme seu endereço: '))
        time.sleep(1)
        confirmacao = int(input('Deseja confirmar o pedido?\n[1] - Sim\n[2] - Não\n'))
        time.sleep(1)
        if confirmacao == 2:
            print('Escolha novamente')
        elif confirmacao == 1:
            print(f'Total - R${preco_sabor + preco_bebida}\n' + '-' * 15)
            time.sleep(1)
            print(f'Entrega para {nome} no endereço abaixo:\n{endereco}\n' + '-' * 15)
            time.sleep(1)
            pagamento()
            print('-' * 15 + '\nObrigado nos escolher!')
            break
        else:
            print('Opçao Inválida')
