#Escreva um programa de autenticação que receba um nome de usuário e senha (input) informe se:
    #Autenticação foi bem-sucedida.
    #Se o nome de usuário não existe.
    #Se a senha está incorreta.
#Os valores corretos de nome de usuário e senha devem estar armazenados em constantes, como no exemplo abaixo:
    #USUARIO = "ADMIN"
    #SENHA = "123123"

USUARIO = "ADMIN"
SENHA = "123123"

nome_usuario = input("Digite o nome do usuario: \n")
senha_usuario = input("Digite a senha: \n")


if(USUARIO == nome_usuario) and (SENHA == senha_usuario):
    print("Autenticação foi bem-sucedida")
elif nome_usuario != USUARIO:
    print("Usuário não existe")
    
elif senha_usuario != SENHA:
    print("Senha incorreta")
