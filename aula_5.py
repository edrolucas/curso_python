#O programa recebe um número interiro e imprime
    #“Fizz", caso o número seja múltiplo de 3.
    #“Buzz", caso o número seja múltiplo de 5.
    #“FizzBuzz", caso o número seja múltiplo de 3 e de 5.

Numero = int(input("Digite um numero: \n"))

Fizz = (Numero % 3 == 0)
Buzz = (Numero % 5 == 0)
FizzBuzz = Fizz and Buzz

if Fizz:
    (print(Numero, "--> Fizz"))

elif Buzz:
    (print(Numero, "--> Buzz"))

elif FizzBuzz:
    (print(Numero, "--> FizzBuzz"))

else:
    print(Numero, '-->')