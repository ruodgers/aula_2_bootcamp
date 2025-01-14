# #Exercicio 211#
# # try-except - Escreva um porgrama que converrta temperatura de Celsius apra Fahrenheit.
# try:
#     celsius = float(input("insira a temperatura atual em graus Celsius: "))
#     fahrenheit = ((celsius* (9/5)) + 32)
#     print(f"{celsius}ºC é igual a {fahrenheit}ºF.")
# except ValueError:
#     print("insira apenas números")

# # #Exercicio 22
# # # if, elif, else
# # entrada = input("Insira um palídromo: ")


# # if isinstance(entrada, str):
# #     formatada = entrada.replace(" ", "").lower()
# #     if formatada == formatada[::-1]:
# #         print('É um palídromo.')
# #     else:
# #             print("Não é um palíndromo")
# # else:
# #      print("Entrada inválida. Por favor, digite uma palvra ou frase")

# #Exercicio 23
# # try, if, elif, else, except
# # try:
# #     num_1 = float(input("digite um valor:"))
# #     num_2 = float(input("digite outro valor:"))
# #     operador = input("digite um operador(+, - ,* ,/):")
# #     if operador == "+":
# #         resultado = num_1 + num_2
# #     elif operador == "-":
# #         resultado = num_1 - num_2
# #     elif operador == "*":
# #         resultado = num_1 * num_2
# #     elif operador == "/" and num_2 != 0:
# #         resultado = num_1 / num_2 
# #     else:
# #         print("Operador invalido ou divisão por zero")
# #     print(f"Resultado:", resultado)
# # except ValueError:
# #     print("Erro. Entrada Inválida. Certifique-se de inserir apenas números")  

# #exercicio 24 
# ##Escreva um programa que solicite ao usuário para digitar um número. 
# # Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
# # Adicionalmente, identifique se o número é "par" ou "ímpar".
# try:
#     valor = float(input("insira um um número inteiro qualquer: "))
#     if valor > 0:
#         print("você digitou um número positivo.")
#     elif valor < 0:
#         print("OVocê digitou um número negativo.")
#     else:
#         print("Você digitou 0.")

# ##verificar se é par ou ímpar?
#     if valor % 2 == 0:
#         print("O número é par.")
#     elif valor % 2 == 1:
#         print("O número é ímpar")
#     else:
#         print("Você digitou um número decimal. Números decimais não podem ser classificados em pares ou ímpares.")

# except ValueError:
#     print("Você não digitou um número.")


#Crie um programa que pede a inserção de uma lista de números separada separados por vírgulas.
# O programa deverár converter de str para uma lsita de inteiros. Use try-except.

lista_str = input("insira uma lista de números separados por vírgula: ")
numeros_str = lista_str.split(",")
numeros_int = []

try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de números inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os números da lista são inteiros válidos")