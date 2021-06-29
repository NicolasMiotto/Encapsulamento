from Pessoa import Pessoa
from Juridica import Juridica
from Fisica import Fisica

print("=-=-=-=-=-=-=Pessoa=-=-=-=-=-=-=")
p1 = Pessoa(1,"Nicolas", "Av. America", 69846633)
p1.imprimir_nome()
p1.imprimir_telefone()

print("=-=-=-=-=-=-=Pessoa Física=-=-=-=-=-=-=")
pf1 = Fisica(2, "João", "R. Cristovao", 99668855, "65863548598", 25 , 99, 1.95)
imc = pf1
imc.calcula_IMC()
pf1.imprimir_cpf()

print("=-=-=-=-=-=Pessoa Jurídica=-=-=-=-=-=")
print("=-=-=-=-=-=Nota fiscal=-=-=-=-=-=-=")
pj1 = Juridica(3, "Makana materiais artisticos LTDA", "Rua Mariante", 33698755 ,"1526845768486", "Regulamentado", 230)
pj1.emitir_nota_fiscal()
pj1.imprimir_cnpj()