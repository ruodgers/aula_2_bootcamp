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


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# import math
# print("exercicio 10")
# raio = float(input("Digite o raio de um circulo: "))
# pi = math.pi
# area_do_circulo = pi*(raio**2)
# print("A área do círculo é", (f"{area_do_circulo:.2f}"))

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
print("exercicio 14")
data_nasc = input("insira sua data de nascimento no formato dd/mm/aaaa: ")
lista_dia_mes_ano = data_nasc.split("/")
print(lista_dia_mes_ano)


print("ou") 

data_nasc = input("insira sua data de nascimento no formato dd/mm/aaaa: ")
lista_dia_mes_ano = data_nasc.split("/")
print(f"O dia é", {lista_dia_mes_ano [0]})
print(f"O mês é", {lista_dia_mes_ano [1]})
print(f"O ano é", {lista_dia_mes_ano [2]})

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
