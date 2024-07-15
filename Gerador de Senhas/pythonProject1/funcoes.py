from random import choice  # Importa função "choice" da biblioteca "random"
from time import sleep  # Importa função "sleep" da biblioteca "time"

# Cria uma lista vazia para armazenar as senhas
senha = []


# Função para ler se o valor digitado é um número inteiro
def ler_inteiro(inteiro):
    while True:
        try:
            inteiro = int(input(inteiro))

        except (TypeError, ValueError):
            print('Digite um número inteiro')
            continue
        else:
            return inteiro
            break


# Função para inserir a quantidade de senhas desejada
def qtdd_senha():
    qtdd = ler_inteiro('Quantidade de senhas: ')
    return qtdd


# Função para inserir o tamanho da senha desejada
def tam_senha():
    tamanho = ler_inteiro('Tamanho da senha: ')
    return tamanho


# Função para gerar as senhas, vamos armazenar os caracteres em um dict para poder criar a senha
def gerar_senhas(qtdd, tam):
    print('Gerando senhas...')
    sleep(1)

    caracteres = (
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w",
        "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
        "T",
        "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "&",
        "*")

    # Repetição para contar o tamanho da senha e a quantidade
    for senha_gerada in range(0, int(qtdd)):
        for string in range(0, int(tam)):
            senha.append(choice(caracteres))

        for caracter in senha:
            print(caracter, end='')

        print('')
        senha.clear()
