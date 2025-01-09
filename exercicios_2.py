# #Exercicio 211#
# # try-except - Escreva um porgrama que converrta temperatura de Celsius apra Fahrenheit.
# try:
#     celsius = float(input("insira a temperatura atual em graus Celsius: "))
#     fahrenheit = ((celsius* (9/5)) + 32)
#     print(f"{celsius}ºC é igual a {fahrenheit}ºF.")
# except ValueError:
#     print("insira apenas números")

# #Exercicio 22
# # if, elif, else
# entrada = input("Insira um palídromo: ")


# if isinstance(entrada, str):
#     formatada = entrada.replace(" ", "").lower()
#     if formatada == formatada[::-1]:
#         print('É um palídromo.')
#     else:
#             print("Não é um palíndromo")
# else:
#      print("Entrada inválida. Por favor, digite uma palvra ou frase")

#Exercicio 23
# try, if, elif, else, except
try:
    num_1 = float(input("digite um valor:"))
    num_2 = float(input("digite outro valor:"))
    operador = input("digite um operador(+, - ,* ,/):")
    if operador == "+":
        resultado = num_1 + num_2
    elif operador == "-":
        resultado = num_1 - num_2
    elif operador == "*":
        resultado = num_1 * num_2
    elif operador == "/" and num_2 != 0:
        resultado = num_1 / num_2 
    else:
        print("Operador invalido ou divisão por zero")
    print("Resultado:", resultado)
except ValueError:
    print("Erro. Entrada Inválida. Certifique-se de inserir apenas números")   