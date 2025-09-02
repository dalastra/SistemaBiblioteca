class Livro: #cria um molde
    def __init__(self, nome, autor, genero, situacao="Disponível"): #o "_init_" é o construtor, ele é executado sempre quando um livro novo é criado
        self.__nome = nome #"set" é a forma de dizer que aquele dado pertence ao objeto específico
        self.__autor = autor
        self.__genero = genero
        self.__situacao = situacao #os dois underlines significa que eles não podem ser acessados diretamente fora da classe

# ----------------- -------------------------
    #Metodos GETs && SETs

    def getNome(self): #"get" pega as informações dos atributos privados
        return self.__nome
    
    def getAutor(self):
        return self.__autor
    
    def getGenero(self):
        return self.__genero
    
    def getSituacao(self):
        return self.__situacao
    
    def setNome(self, nome): #"set" é usado para alterar as informações, um exemplo é alterar de "Disponível" para "Emprestado"
        self.__nome = nome
        return self.__nome
    
    def setAutor(self, autor):
        self.__autor = autor
        return self.__autor
    
    def setGenero(self, genero):
        self.__genero = genero
        return self.__genero

    def setSituacao(self, situacao):
        self.__situacao = situacao
        return self.__situacao
