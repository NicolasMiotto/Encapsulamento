from Pessoa import Pessoa

class Fisica(Pessoa):

    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.imc = 0

    def imprimir_cpf(self):
        print("CPF: ", self.cpf)

    def calcula_IMC(self):
        self.imc = self.peso / (self.altura * self.altura)
        print("Nome: ", self.nome)
        print("O IMC de %s é %f" % (self.nome, self.imc))
   
