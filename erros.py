# # TypeError - Ocorre quando uma operação ou função é aplicada a um objeto de tipo inadequado
# # Exemplo
# try:
#     resultado = len(5)
# except TypeError as e:
#     print(e) #imprime a mensagem de erro


#Type Check - verificação do tipo de vairável. pode usar type() ou isinstance()
# #exemplo
# idade = "babuino"
# if isinstance(idade, int):
#     print("A variável é um inteiro")
# else:
#     print("A variável não é um inteiro", type(idade)) #além de retornar que não é um inteiro, retorna qual o tipo.

#Type Conversion - Conversão de tipo ou casting, permite a conversão de um tipo de variável para outro, por meio de uma converão explícita como str(), float(), int(), etc.
# # exemplo: soma de um inteiro com um flutuante
# inteiro = 5
# flutuante = 2.5
# #converte o inteiro para flutuante e realiza a soma
# soma = float(inteiro) + flutuante
# print(soma) 

#try-except - usada para tratamento de exceções em python. Exceções são erros que ocorrem ao longo do código e se não tatado, interrompe o fluxo e encerra a execução
# O tratamento de exceções permite que o programa lide com erros de forma elegante e continue a execção sem falhas
## Try: é o primeiro bloco para tratar exceções
## except: se algo ocorre dentro do bloco try, a execução pula para o bloco except. é necessário especificar os tipos exceções.
#específicos para poder tratá-las. Se não forem especificadas, toda serão capturadas.
# exemplo
# try:
#     # código que pode gerar uma exceção
#     resultado = 10 / 0
# except ZeroDivisionError:
#     #código que executa se a exceção ZeroDivisorError for levantada
#     print("Divisão por zero não é permitida")


# #outro exemplo
# num_1 = int(input("Insira um número: "))
# num_2 = (input("Insira outro número: "))
# try:
#     divide = num_1 / int(num_2)
#     (print(divide))
# except ZeroDivisionError:
#     print("Impossível dividir por zero")
# except TypeError:
#     print("Tipo de dado informado não permite divisão")


#if - estrutura que permite executar diferenntes ações com base em condições.
    #if - Avalia a condições, Se for True, o bloco será executado, se for False, o bloco será ignorado
    #elife -abreviação de else if, que permite verificar múltiplas condições em sequencia
    ##else - executa um bloco se todas as condiçõea anteriores if e elif forem falsas

#exemplo
# idade = input("Insira a sua idade (apenas números): ")
# try:
#     if int(idade) < 18:
#         print("Menor de idade")
#     elif int(idade) == 18:
#      print("Exatamente 18 anos")
#     else:
#        print("Maior de Idade")
# except ValueError:
#    print("Você não digitou somente números")

