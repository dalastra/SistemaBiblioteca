import os #importa a biblioteca
from classes import * #importa tudo que tem em classes.py

livros = { #diconário de livros ja cadastrados
    1 : Livro("Dom Casmurro", "Machado de Assis", "Romance","Emprestado"),
    2 : Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", "Romance"),
    3 : Livro("Quincas Borba", "Machado de Assis", "Romance"),
    4 : Livro("Frankenstein", "Mary Shelley", "Terror"),
    5 : Livro("Drácula", "Bram Stoker", "Terror"),
    6 : Livro("Evangelho de Sangue", "Clive Barker", "Terror","Emprestado"),
    7 : Livro("Morangos Mofados", "Caio Fernando Abreu", "Contos"),
    8 : Livro("O Alienista", "Machado de Assis", "Contos"),
    9 : Livro("O Cartomante", "Machado de Assis", "Contos"),
    10 : Livro("Marília de Dirceu", "Tomás Antônio Gonzaga", "Poesia"),
    11 : Livro("Toda Poesia", "Paulo Leminski", "Poesia","Emprestado"),
    12 : Livro("Os Lusíadas", "Luís de Camões", "Poesia"),
    13 : Livro("Alguma Poesia", "Carlos Drummond de Andrade", "Poesia"),
    14 : Livro("Star Wars: Marcas da Guerra", "Chuck Wendig", "Ação"),
    15 : Livro("A Bússola de Ouro", "Philip Pullman", "Ação","Emprestado"),
    16 : Livro("Ponto de Impacto", "Dan Brown", "Ação","Emprestado"),
    17 : Livro("Apologia de Sócrates", "Platão", "Filosofia"),
    18 : Livro("O Príncipe", "Maquiavel", "Filosofia"),
    19 : Livro("A República", "Platão", "Filosofia","Emprestado"),
    20 : Livro("Os Dois Morrem no Final", "Adam Silvera", "Infanto Juvenil"),
    21 : Livro("Retórica", "Aristóteles", "Filosofia"),
    22 : Livro("O Diário de Anne Frank", "Anne Frank", "História"),
    23 : Livro("Sapiens: Uma Breve História da Humanidade", "Yuval Noah Harari", "História"),
    24 : Livro("Diário de um Banana", "Jeff Kinney", "Infanto Juvenil","Emprestado"),
    25 : Livro("As Crônicas de Nárnia", "C. S. Lewis", "Infanto Juvenil"),
    26 : Livro("Pedagogia do Oprimido", "Paulo Freire", "Filosofia","Emprestado"),
    27 : Livro("Tópicos", "Aristóteles", "Filosofia"),
    28 : Livro("Crítica da Razão Pura", "Immanuel Kant", "Filosofia","Emprestado"),
    }


def adicionar(livros): #adiciona livros no sistema
        os.system("cls")
        nome = input("Informe o NOME do livro: ") #recebe as informações do livro que sera adicionado
        autor = input("Informe o AUTOR do livro: ")
        genero = input("Informe o GÊNERO do livro: ")
        
        livros[len(livros) + 1] = Livro(nome=nome, autor=autor, genero=genero) # adiciona o livro dentro do dicionário, a situação do livro ja vem como padrão "Disponível"
        print("* Livro adicionado com sucesso! *\n")
        os.system("pause")


def remover(livros): #remove os livros do sistema
    os.system("cls")
    if not livros: # se não houver nenhum livro cadastrado ele retorna ao menu inicial
        print("Nenhum livro cadastrado!")
        os.system("pause")
        return
    listartudo(livros=livros)
    remover = int(input("\nDigite o NÚMERO do livro que deseja remover\n-->  "))
    if remover in livros:
        removido = livros.pop(remover) #remove o livro do dicionário usando a função pop
        print(f"\nLivro '{removido.getNome()}' removido com sucesso!")


def listartudo(livros):
    os.system("cls")
    if not livros:
        print("Nenhum livro cadastrado!")
        os.system("pause")
        return
    os.system("cls")
    print("--- LISTA DE LIVROS ---")
    print("")
    for chave, valor in livros.items(): # lista todos os livros que tem no dicionário
        print(f"{chave}° - \tNome --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n\tGênero --> {valor.getGenero()}\n\tSituação --> {valor.getSituacao()}\n")
    os.system("pause")


def listar(livros):
    os.system("cls")
    if not livros:
        print("Nenhum livro cadastrado!")
        os.system("pause")
        return
    os.system("cls")
    print("--- COMO VOCÊ DESEJA LISTAR OS LIVROS? ---")
    print("")
    deseja = int(input("1 - Autor\n2 - Gênero\n3 - Livros emprestados\n\n--> ")) #escolhe a forma de como deseja listar
    if deseja == 1:
        listarautor(livros=livros)
    elif deseja == 2:
        listargenero(livros=livros)
    elif deseja == 3:
        listaremprestados(livros=livros)
    

def listarautor(livros):
    os.system("cls")
    if not livros:
        print("Nenhum livro cadastrado!")
        os.system("pause")
        return
    os.system("cls")
    print("--- LISTA DE LIVROS POR AUTOR ---")
    print("")
    print("1 - Machado de Assis\n2 - Mary Shelley\n3 - Bram Stoker\n4 - Clive Barker\n5 - Caio Fernando Abreu\n6 - Tomás Antônio Gonzaga\n7 - Paulo Leminski\n8 - Luís de Camões\n9 - Carlos Drummond de Andrade\n10 - Chuck Wendig\n11 - Philip Pullman\n12 - Dan Brown\n13 - Platão\n14 - Maquiavel\n15 - Adam Silvera\n16 - Aristóteles\n17 - Anne Frank\n18 - Yuval Noah Harari\n19 - Jeff Kinney\n20 - C. S. Lewis\n21 - Paulo Freire\n22 - Immanuel Kant\n")
    escolha_aut = int(input("Informe o NÚMERO do autor que você deseja listar --> "))
    os.system("cls")
    if escolha_aut == 1:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Machado de Assis":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause") 
    elif escolha_aut == 2:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Mary Shelley":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 3:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Bram Stoker":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 4:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Clive Barker":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 5:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Caio Fernando Abreu":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 6:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Tomás Antônio Gonzaga":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 7:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Paulo Leminski":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 8:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Luís de Camões":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 9:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Carlos Drummond de Andrade":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 10:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Chuck Wendig":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 11:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Philip Pullman":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 12:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Dan Brown":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 13:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Platão":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 14:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Maquiavel":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 15:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Adam Silvera":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 16:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Aristóteles":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 17:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Anne Frank":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 18:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Yuval Noah Harari":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 19:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Jeff Kinney":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 20:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "C. S. Lewis":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 21:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Paulo Freire":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_aut == 22:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getAutor() == "Immanuel Kant":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tAutor --> {valor.getAutor()}\n")
                encontrou = True
        os.system("pause")


def listargenero(livros):
    os.system("cls")
    if not livros:
        print("Nenhum livro cadastrado!")
        os.system("pause")
        return
    os.system("cls")
    print("--- LISTA DE LIVROS POR GÊNERO ---")
    print("")
    print("1 - Romance\n2 - Terror\n3 - Contos\n4 - Poesia\n5 - Ação\n6 - Filosofia\n7 - Infanto Juvenil\n8 - História")
    escolha_gen = int(input("Informe o NÚMERO do gênero que você deseja listar --> "))
    os.system("cls")
    if escolha_gen == 1:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getGenero() == "Romance":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tGênero --> {valor.getGenero()}\n")
                encontrou = True
        os.system("pause") 
    elif escolha_gen == 2:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getGenero() == "Terror":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tGênero --> {valor.getGenero()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_gen == 3:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getGenero() == "Contos":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tGênero --> {valor.getGenero()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_gen == 4:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getGenero() == "Poesia":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tGênero --> {valor.getGenero()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_gen == 5:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getGenero() == "Ação":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tGênero --> {valor.getGenero()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_gen == 6:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getGenero() == "Filosofia":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tGênero --> {valor.getGenero()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_gen == 7:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getGenero() == "Infanto Juvenil":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tGênero --> {valor.getGenero()}\n")
                encontrou = True
        os.system("pause")
    elif escolha_gen == 8:
        encontrou = False
        for chave, valor in livros.items():
            if valor.getGenero() == "História":
                print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tGênero --> {valor.getGenero()}\n")
                encontrou = True
        os.system("pause")
    

def listaremprestados(livros):
    os.system("cls")
    if not livros:
        print("Nenhum livro cadastrado!")
        os.system("pause")
        return
    os.system("cls")
    print("--- LISTA DE LIVROS POR EMPRÉSTIMO ---")
    print("")
    encontrou = False
    for chave, valor in livros.items():
        if valor.getSituacao() == "Emprestado":
            print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tSituação --> {valor.getSituacao()}\n")
            encontrou = True
    os.system("pause")


def atualizar(livros):
    os.system("cls")
    if not livros:
        print("Nenhum livro cadastrado!")
        os.system("pause")
        return
    listartudo(livros=livros)

    alterar = int(input("Informe o NÚMERO do livro que deseja alterar\n--> "))
    caracteristica = int(input("Qual caracteristica quer alterar\n1 - Nome\n2 - Autor\n3 - Gênero\n--> "))
    os.system("cls")
    if caracteristica == 1:
        nome = input("Informe o nome do livro\n--> ")
        livros[alterar].setNome(nome)
    elif caracteristica == 2:
        autor = input("Informe o autor do livro\n--> ")
        livros[alterar].setAutor(autor)
    elif caracteristica == 3:
        genero = input("Informe o gênero do livro\n--> ")
        livros[alterar].setGenero(genero)
    listartudo(livros=livros)


def emprestar(livros):
    os.system("cls")
    if not livros:
        print("Nenhum livro cadastrado!")
        os.system("pause")
        return
    print("--- LISTA DE LIVROS DISPONÍVEIS ---")
    print("")
    encontrou = False
    for chave, valor in livros.items():
        if valor.getSituacao() == "Disponível":
            print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tSituação --> {valor.getSituacao()}\n")
            encontrou = True
    os.system("pause")
    alterar = int(input("Informe o NÚMERO do livro que deseja emprestar\n--> "))
    if alterar not in livros:
        print("Número inválido!")
        os.system("pause")
        return
    if livros[alterar].getSituacao() == "Emprestado":
        os.system("cls")
        print("Esse livro já está emprestado!")
        os.system("pause")
        return
    situacao = int(input("Emprestar livro\n1 - Sim\n2 - Não\n\n--> "))
    os.system("cls")
    if situacao == 1:
        livros[alterar].setSituacao("Emprestado")
        print("Empréstimo feito com sucesso!")
        os.system("pause")
    else:
        print("Empréstimo cancelado...")
        os.system("pause")
        return
    

def devolver(livros):
    os.system("cls")
    if not livros:
        print("Nenhum livro cadastrado!")
        os.system("pause")
        return
    print("--- LISTA DE LIVROS EMPRESTADOS  ---")
    print("")
    encontrou = False
    for chave, valor in livros.items():
        if valor.getSituacao() == "Emprestado":
            print(f"{chave}° - \tLivro --> {valor.getNome()}\n\tSituação --> {valor.getSituacao()}\n")
            encontrou = True
    alterar = int(input("Informe o NÚMERO do livro que deseja fazer a devolução\n--> "))
    if alterar not in livros:
        print("Número inválido!")
        os.system("pause")
        return

    if livros[alterar].getSituacao() == "Disponível":
        os.system("cls")
        print("Esse livro já foi devolvido!")
        os.system("pause")
        return
    
    else:
        livros[alterar].setSituacao("Disponível")
        print("Devolução feita com sucesso!")
        os.system("pause")
    
    
def menu():

#menu
    while True:
        os.system("cls")
        print("BEM VINDO A BIBLIOTECA LIVROTECH\n1 - Adicionar livro\n2 - Remover livro\n3 - Listar todos os livros\n4 - Listar livros por preferência\n5 - Editar detalhes\n6 - Emprestar livro\n7 - Devolver livro\n8 - Sair")
        escolha = int(input("\nEscolha a opção desejada --> "))    

        if escolha == 1:
            adicionar(livros=livros)
        elif escolha ==2:
            remover(livros=livros)
        elif escolha == 3:
            listartudo(livros=livros)
        elif escolha == 4:
            listar(livros=livros)
        elif escolha == 5:
            atualizar(livros=livros)
        elif escolha == 6:
            emprestar(livros=livros)
        elif escolha == 7:
            devolver(livros=livros)
        elif escolha == 8:
            os.system("cls")
            print("SAINDO...")
            break
        else:
            print("ESCOLHA INVALIDA")
            os.system("pause")