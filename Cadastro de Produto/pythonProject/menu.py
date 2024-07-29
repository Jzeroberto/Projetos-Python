from tkinter import *

from cadastro import Cadastro
from lista import ListaProtudos


class Menu:
    def __init__(self, master=None):
        self.cadastro_instance = None
        self.lista_produtos_instance = None
        self.master = master
        self.master.title('Menu')
        self.master.geometry('200x200+860+440')

        self.cadastrarContainer = Frame(master)
        self.cadastrarContainer['pady'] = 10
        self.cadastrarContainer.pack()

        self.listaContainer = Frame(master)
        self.listaContainer['pady'] = 10
        self.listaContainer.pack()

        self.botaoCadastrar = Button(self.cadastrarContainer, text='Cadastro de Produto', command=self.abrir_cadastro)
        self.botaoCadastrar.pack()

        self.listaContainer = Button(self.listaContainer, text='Lista de Produtos', command=self.abrir_lista_produtos)
        self.listaContainer.pack()
        
    def abrir_cadastro(self):
        self.cadastro_instance = Toplevel(self.master)
        Cadastro(self.cadastro_instance, self.master)
        self.master.withdraw()

    def abrir_lista_produtos(self):
        self.lista_produtos_instance = Toplevel(self.master)
        ListaProtudos(self.lista_produtos_instance, self.master)
        self.master.withdraw()
