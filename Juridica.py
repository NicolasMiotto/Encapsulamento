from Pessoa import Pessoa

class Juridica(Pessoa):

    def __init__(self, codigo, nome, endereco, telefone, cnpj, inscricao_estadual, qtdFuncionarios):
        Pessoa.__init__(self,codigo, nome, endereco, telefone)
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual
        self.qtdFuncionarios = qtdFuncionarios


    def emitir_nota_fiscal(self):
        print("Nome: ",self.nome )
        print("Incrição Estadual: ", self.inscricao_estadual)
        print("Telefone: ", self.telefone)

    def imprimir_cnpj(self):
        print("CNPJ:", self.cnpj)