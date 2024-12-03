#Implemente uma calculadora que recebe 3 valores do usuário:
#
#Operando a (pode ser um inteiro ou float).
#Operando b (pode ser um inteiro ou float).
#Operador op.
#op pode ser uma string representando o operador, por exemplo, "+" ou "-". 
# Outra opção é utilizar números, por exemplo, 1 para soma, 2 para subtração, etc.
#O seu programa deve receber esses 3 valores e imprimir o resultado da operação. 
# Caso o operador seja de divisão e o segundo operando seja o valor zero, o programa deve imprimir uma mensagem: 
# “Não é possível realizar divisão por zero!”.

a = float(input("Digite o primeiro valor: \n"))
b = float(input("Digite o segundo valor: \n"))
op = input("Operador logico: \n")


if op == "+":
    Resultado = a+b

elif op == "-":
    Resultado = a-b

elif op == "*":
    Resultado = a*b

#Não tinha me ligado na hora que poderia usar um if dentro de um elif    
elif op == "/" :     
  if b == 0:
      Resultado = "Não é possivel realizar divisao por zero"
else:
    Resultado = a/b

print(Resultado)