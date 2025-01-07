##sempre que houver intereção com usuário, é necessário prever os erros cometidos por ele no código, a fim de que o programa continue funcionando



# # 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# try:
#     print("exercicio 4")
#     valor_a = int(input("Digite um número inteiro: "))
#     valor_b = int(input("Digite outro número inteiro: "))
#     resultado = valor_a // valor_b
#     print("O quociente inteiro dos dois valores é", resultado)
# except ZeroDivisionError:
#     print("impossível dividor por zero")
# except KeyboardInterrupt:
#     print("acho que você não quis inserir um número")
# except(ValueError):
#     print("por favor, insira apenas números inteiros")


# ##Type Error, else e finally
# try: 
#     nome = "Roger"
#     resultado = len(3)
#     print(resultado)
# except TypeError as e:
#     print(e) #imprime a mensagem de erro
# else:
#     print("tudo ocorreu bem")
# finally:
#     print("o importante é participar")


# ## if isistance - pare verificar  o tipo de variável (pode usar o type também) e retorna uma mensagem apropriada
# numero = print(input("insira um número: "))
# if isinstance (numero, int):
#     print("A variável é um inteiro.")
# else:
#     print("A variável não é um inteiro")


#if avalia a condição. Se a condição for satisfeita, ele executa, se não for satisfeita, ele ignora o bloco
#elif adiciona mais de uma condição
idade = 20
if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("exatamente 18 anos")
else:
    print("Maior de idade")
