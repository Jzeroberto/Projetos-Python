from tkinter import *

from cadastro import produtos


class ListaProtudos:
    def __init__(self, master, menu_instance):
        self.menu_instance = menu_instance
        self.master = master
        self.master.title('Lista dos Produtos')
        self.master.geometry('200x200+860+440')

        self.listaContainer = Frame(master)
        self.listaContainer['pady'] = 10
        self.listaContainer.pack()

        self.listaboxContainer = Frame(master)
        self.listaboxContainer['pady'] = 10
        self.listaboxContainer.pack()

        self.listaLabel = Label(self.listaContainer, text='Produtos')
        self.listaLabel.pack()

        self.listaboxListbox = Listbox(self.listaboxContainer)
        self.listaboxListbox.pack()

        self.atualizar_lista()

    def atualizar_lista(self):
        for produto in produtos:
            self.listaboxListbox.insert(END, produto)





