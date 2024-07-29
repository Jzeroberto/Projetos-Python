from tkinter import *

produtos = []
categorias = []


class Cadastro:
    def __init__(self, master, menu_instance):
        self.menu_instance = menu_instance
        self.master = master
        self.master.title('Cadastro de Produto')
        self.master.geometry('200x200+860+440')

        self.produtoContainer = Frame(master)
        self.produtoContainer['pady'] = 10
        self.produtoContainer.pack()

        self.categoriaContainer = Frame(master)
        self.categoriaContainer['pady'] = 10
        self.categoriaContainer.pack()

        self.botaoContainer = Frame(master)
        self.botaoContainer['pady'] = 10
        self.botaoContainer.pack()

        self.labelProduto = Label(self.produtoContainer, text='Nome do Produto')
        self.labelProduto.pack()

        self.entryProduto = Entry(self.produtoContainer)
        self.entryProduto.pack()

        self.labelCategoria = Label(self.categoriaContainer, text='Categoria do Produto')
        self.labelCategoria.pack()

        self.entryCategoria = Entry(self.categoriaContainer)
        self.entryCategoria.pack()

        self.botaoCadastrar = Button(self.botaoContainer, text='Cadastrar', command=self.cadastrar_produto)
        self.botaoCadastrar.pack()

        self.botaoVoltar = Button(self.botaoContainer, text='Voltar', command=self.voltar_menu)
        self.botaoVoltar.pack()

    def voltar_menu(self):
        self.master.destroy()
        self.menu_instance.deiconify()

    def cadastrar_produto(self):
        global produtos
        global categorias
        produto = self.entryProduto.get()
        categoria = self.entryCategoria.get()
        produtos.append({produto})
        categorias.append({categoria})
        self.entryProduto.delete(0, END)
        self.entryCategoria.delete(0, END)


