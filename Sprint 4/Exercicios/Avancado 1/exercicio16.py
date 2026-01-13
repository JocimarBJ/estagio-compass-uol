class Pessoa:
    def __init__(self, id):
        self.__nome = None  # atributo privado
        self.id = id        # atributo público
        
    # Getter
    @property
    def nome(self):
        return self.__nome

    # Setter
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
