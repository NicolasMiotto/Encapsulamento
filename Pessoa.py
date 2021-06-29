class Pessoa():
    def __init__(self,codigo, nome, endereco, telefone):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def imprimir_nome(self):
        print("Nome: ", self.nome)

    def imprimir_telefone(self):
        print("Telefone: ", self.telefone)