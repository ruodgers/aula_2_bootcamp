# # #### Inteiros (`int`)

# # 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
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

# # # #### Números de Ponto Flutuante (`float`)

# # 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# print("exercicio 6")
# flut1 = float(input("Digite um número decimal: "))
# flut2 = float(input("Digite outro número decimal: "))
# resultado = flut1 + flut2

# print("A soma dos números é", resultado)


# # 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.]
# print("exercicio 7")
# valor_a = float(input("Insira um número decimal: "))
# valor_b = float(input("Insira outro número decimal: "))
# print(("A média dos valores é de", valor_a + valor_b)/2) #poderia ter criado uma variável chamada média que contém o cálculo e depoiss printar apenas o resultado dela

# # 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# print("exercicio 8")
# base = float(input("insira um número: "))
# expoente = int(input("insira um valor de expoente: ")) # poderia ter criado uma nova variavel que recebe o calculo e depois apenas imprimir

# print("O valor da potenciação é", base**expoente)

# # # 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# print("exercicio 9")
# temp_c = float(input("Insira a temperatura atual em graus Celsius: "))
# temp_f = (temp_c* 9/5) + 32
# print("A temperatura em graus Fahrenheit é", temp_f )

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# import math
# print("exercicio 10")
# raio = float(input("Digite o raio de um circulo: "))
# pi = math.pi
# area_do_circulo = pi*(raio**2)
# print("A área do círculo é", (f"{area_do_circulo:.2f}"))


# #ou 
# raio = 5.0
# area = 3.1459 * raio * 2
# print("A área do círculo é", area)

# # # #### Strings (`str`)

# # 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# nome = input("insira o seu nome e lestras minúsculas: ")
# print(nome.upper())

# # 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# print("exercicio 12")
# nome = (input("insira o seu nome completo em maísculo: "))
# print(nome.lower()) # poderia usar uma varíavel com o noem inputado, outra com o nome processado e imprimido este último


# # 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# print("exercicio 13")
# frase = input("escreva uma frase adicionando 3 espaços no início e no final: ")
# print(frase.strip()) # frase sem espaço

# #14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
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

# #outro método que pode ser utilizado é o desempacotamento
# data_nasc = input("insira sua data de nascimento no formato dd/mm/aaaa: ")
# dia, mes, ano = data_nasc.split("/")
# print("Dia é:", dia)
# print("Mês é:", mes)
# print("Ano é:", ano)

# # 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# print("exercicio 15")
# nome = input("insira o seu primeiro nome: ")
# sobrenome = input("insira o seu ultimo nome: ")
# print(nome + " " + sobrenome) #posso concatenar variáveis com vírgulas que o expaço será adicionado automaticamente


# #ou
# nome = input("insira o seu primeiro nome: ")
# sobrenome = input("insira o seu ultimo nome: ")
# print(nome, sobrenome)




# #### Booleanos (`bool`)

# # 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# print("exercicio 16")
# valor_1 = bool(input("Insira a palavra True: "))
# valor_2 = bool(input("Insira a palavra False: "))
# bool_and = valor_1 and valor_2
# print(bool_and)
 


# # 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# print("exercicio_17")
# bool_or = valor_1 or valor_2
# print(bool_or)

# # 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# # print("exercicio_18")
# bool_not = not valor_1
# print(bool_not)


# # 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# print("exercicio 19")
# valor_1 = int(input("insira o número 2: "))
# valor_2 = int(input("insira novamente o número 2: "))

# comparado = (valor_1 == valor_2)

# print(comparado)


# # 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# print("exercicio 19")
# valor_1 = int(input("insira o número 2: "))
# valor_2 = int(input("insira o número 3 "))

# comparado = (valor_1 != valor_2)

# print(comparado)



# #### try-except e if

# # 21: Conversor de Temperatura
# print("exercicio 21")

# def conversor_temperatura():
#     temperatura = float(input("insira a temperatura atual: "))
#     unidade = input("insira C para Celsius ou F para Fahrenheit: ").upper()

#     if unidade == "C":
#         #converte Celsius para Fahrenheit
#         resultado = (temperatura * 9/5) + 32
#         print(f"{temperatura}ºC é igual a {resultado}ºF")

#     elif unidade == "F":
#         #converte Celsius para Fahrenheit
#         resultado = (temperatura -32) * 5/9
#         print(f"{temperatura}ºF é igual a {resultado}ºC")

#     else:
#         print("Unidade inválida. Use C ou F")

# conversor_temperatura()


# # 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
