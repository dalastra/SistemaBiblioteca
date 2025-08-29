class Livro:
    #Construtor
    def __init__(self, nome, autor, genero, situacao="Disponível"):
        self.__nome = nome
        self.__autor = autor
        self.__genero = genero
        self.__situacao = situacao

# ----------------- -------------------------
    #Metodos GETs && SETs

    def getNome(self):
        return self.__nome
    
    def getAutor(self):
        return self.__autor
    
    def getGenero(self):
        return self.__genero
    
    def getSituacao(self):
        return self.__situacao
    
    def setNome(self, nome):
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