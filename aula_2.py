#Basicamente um estudo sobre tipos de valores e variaveis
#Aprendendo a declarar uma variavel em python



valor_compras = float(input('Digite o valor total das compras:'))
desconto = float(input('Digite o valor do desconto:'))
quantidade_itens = int(input('Digite a quantidade de itens que foram comprados:'))

valordesconto = valor_compras * desconto
valorfinal =  valor_compras - valordesconto

custo_medio = valorfinal / quantidade_itens



print( 'O valor do custo medio é : ' + str(custo_medio))
print('O valor final das compras com desconto é : ' + str(valorfinal))
