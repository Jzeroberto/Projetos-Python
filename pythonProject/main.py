from tkinter import *
from funcoes import *


class Login:
    def __init__(self, master):
        self.menu_instance = None
        self.master = master
        self.master.title('Login')

        self.userContainer = Frame(master)
        self.userContainer['padx'] = 10
        self.userContainer.pack()

        self.passwordContainer = Frame(master)
        self.passwordContainer['padx'] = 10
        self.passwordContainer['pady'] = 10
        self.passwordContainer.pack()

        self.botaoContainer = Frame(master)
        self.botaoContainer['pady'] = 20
        self.botaoContainer.pack()

        self.user = Label(self.userContainer, text='Usuário')
        self.user.pack(side=LEFT)

        self.user = Entry(self.userContainer)
        self.user.pack(side=LEFT)

        self.senha = Label(self.passwordContainer, text='Senha')
        self.senha.pack(side=LEFT, padx=4)

        self.senha = Entry(self.passwordContainer)
        self.senha['show'] = '*'
        self.senha.pack(side=LEFT)

        self.logar = Button(self.botaoContainer, text='Logar', command=self.verificar_login_wrapper)
        self.logar.pack()

        self.msg = Label(self.botaoContainer, text='')
        self.msg.pack()

    def verificar_login_wrapper(self):
        user = self.user.get()
        senha = self.senha.get()

        verficacao = verificar_login(user, senha)

        if verficacao == Menu:
            self.menu_instance = Toplevel(self.master)
            Menu(self.menu_instance)
            self.master.withdraw()
        else:
            self.msg['text'] = verficacao


def main():
    root = Tk()
    root.geometry('200x200+860+440')
    Login(root)
    root.mainloop()


if __name__ == '__main__':
    main()
