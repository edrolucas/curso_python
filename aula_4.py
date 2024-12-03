#Esse é o exercicio 4 do modulo 4
#Usei o if de novo para facilitar minha vida

Valor_de_compra = float(input("Digite o valor da compra:\n"))
Valor_do_Frete = float(input("Valor do frete: \n"))
Desconto = float(input('Valor do desconto: \n'))
Cadastro = str(input("Esse bct é cadastrado: \n"))


Valor_total = Valor_de_compra + Valor_do_Frete
Valor_Desconto = Valor_total * Desconto
Valor_Final = Valor_total - Valor_Desconto

if (Valor_total > 100 ) and (Cadastro == "S"):

 print('Valor Final é de', Valor_Final)

else:
    print('Valor do Desconto não aplicado')
    
    