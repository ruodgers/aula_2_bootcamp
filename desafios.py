# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# print("exercicio 1")
# valor1 = int(input("Digite um número: "))
# valor2 = int(input("Digite outro número: "))
# resultado = valor1 + valor2
# print("A soma é", resultado)

# # 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# print("exercicio 2")
# valor = int(input("Digite um número: "))
# resultado = valor % 5
# print("O resto é", resultado)

# # 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# print("exercicio 3")
# valor_a = int(input("Digite um número: "))
# valor_b = int(input("Digite outro número: "))
# resultado = valor_a * valor_b
# print("O produto dos dois valores é", resultado)

# # 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# print("exercicio 4")
# valor_a = int(input("Digite um número inteiro: "))
# valor_b = int(input("Digite outro número inteiro: "))
# resultado = valor_a // valor_b
# print("O quociente inteiro dos dois valores é", resultado)

# # 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# print("exercicio 5")
# valor_p = int(input("Digite um número: "))
# resultado = valor_p**2
# print("O quadrado do número é", resultado)

# # #### Números de Ponto Flutuante (`float`)

# # 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# print("exercicio 6")
# flut1 = float(input("Digite um número decimal: "))
# flut2 = float(input("Digite outro número decimal: "))
# resultado = flut1 + flut2

# print("A soma dos números é", resultado)


# # 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.]

# try:
#     print("exercicio 7")
#     valor_a = float(input("Insira um número decimal: "))
#     valor_b = float(input("Insira outro número decimal: "))
#     print(("A média dos valores é de", valor_a + valor_b)/2)
# except:
#     print(ValueError)

# # 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# print("exercicio 8")
# base = float(input("insira um número: "))
# expoente = int(input("insira um valor de expoente: "))

# print("O valor da potenciação é", base**expoente)

# # # 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# print("exercicio 9")
# temp_c = float(input("Insira a temperatura atual em graus Celsius: "))
# temp_f = ((160 + (9*temp_c))/5)
# print("A temperatura em graus Fahrenheit é", temp_f )

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# import math
# print("exercicio 10")
# raio = float(input("Digite o raio de um circulo: "))
# pi = math.pi
# area_do_circulo = pi*(raio**2)
# print("A área do círculo é", (f"{area_do_circulo:.2f}"))

# # #### Strings (`str`)

# # 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# nome = input("insira o seu nome e lestras minúsculas: ")
# print(nome.upper())

# # 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# print("exercicio 12")
# nome = (input("insira o seu nome completo: "))
# print(nome.upper())


# # 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# print("exercicio 13")
# frase = input("escreva uma frase adicionando 3 espaçops no início e no final: ")
# print(frase.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# print("exercicio 14")
# data_nasc = input("insira sua data de nascimento no formato dd/mm/aaaa: ")
# lista_dia_mes_ano = data_nasc.split("/")
# print(lista_dia_mes_ano)


# print("ou") 

# data_nasc = input("insira sua data de nascimento no formato dd/mm/aaaa: ")
# lista_dia_mes_ano = data_nasc.split("/")
# print(f"O dia do seu nascimento é", {lista_dia_mes_ano [0]})
# print(f"O mês do seu nascimento é", {lista_dia_mes_ano [1]})
# print(f"O ano do seu nascimento é", {lista_dia_mes_ano [2]})

# # 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# print("exercicio 15")
# nome = input("insira o seu primeiro nome: ")
# sobrenome = input("insira o seu ultimo nome: ")
# print(nome + " " + sobrenome)


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# print("exercicio 16")
# ##valores definidos
# nome_def = "roger"
# idade_def = "33"

# #usuário insere os valores
# nome = input("insira o seu nome: ")
# idade = input("insira a sua idade: ")

# #Avalia se a condição inputada é a mesma
# resultado_and = (nome_def == nome) and (idade_def == idade)

# if resultado_and: 
#     print("O nome e a idade estão corretos. Resultado: True")
# else:
#     print("O nome e a idade estão incorretos. Resultado: false")
 


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# print("exercicio_17")
# nome_ri = "roger"
# idade_ri = "33"

# nome = input("insira o seu nome: ")
# idade = input("insira a sua idade: ")

# #Avalia se a condição inputada é a mesma
# resultado_or = (nome_ri == nome) or (idade_ri == idade)

# print(resultado_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# print("exercicio_18")

# valor = bool(input("Se seu nome for roger, digite True. Caso contrário, digite False: "))

# print(not(valor))


# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# print("exercicio 19")
# valor_1 = int(input("insira um número de 0 a 10: "))
# valor_2 = int(input("insira outro número de 0 a 10, podendo ser repetido: "))

# comparado = (valor_1 == valor_2)

# print(comparado)


# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
print("exercicio 19")
valor_1 = int(input("insira um número de 0 a 10: "))
valor_2 = int(input("insira outro número de 0 a 10, podendo ser repetido: "))

comparado = (valor_1 != valor_2)

print(comparado)



# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
