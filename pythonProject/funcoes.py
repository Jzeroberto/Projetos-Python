from menu import Menu


def verificar_login(user, senha):
    if user == 'jose' and senha == '123':
        return Menu
    else:
        return 'Login Inválido'
