#operacaoes com varíaveis inteiras (int)
#soma
print(5+4)

#subtração
print(7-2)

#divisao inteira: ainda que o resultado seja decimal, retornará o maior valor inteiro. em outras palavras, descarta a parte decimal
print( 5//4 )

#divisao: retorna um valor flutuante, mesmo que seja inteiro
print(5/4)

#multiplicação
print(5*4)

#módulo: retorna o resto da divisão`
print(4 % 5)

#operações com varíaveis flutuantes (float)

#adição
print(5.5 + 2.2)

#subtração
print(5.5 - 2.2)

#multiplicação
print(5.5 * 2.2)

#divisão
(5.5 /2.2)

#potenciação
print(5.5**3)


##operações com strings (str)

#.upper (converte para maiúscula)
nome = " RoGer "
print(type(nome))
print(type(" Roger "))
print(nome.upper())

#.lower (coverte para minúsculo)
print(nome.lower())

#.strip (remove espaçoes em branco no início e no final)
print(nome.strip())

#.split(sep) (divid a string em uma lista, utilizando sep como separador
e_mail = "ruodgers@gmail.com"
print(e_mail.split("@"))\

# + (concatena strings)
nome_user = "Roger" 
idade = "33"
print(nome_user + ", " + idade)

##Booleanos (bol)
#and (E Lógico (conjução do rlm)) - Só é True se tudo for True. Todos os outros são False
valor1 = True
valor2 = False

print(valor1 and valor1)

#or (OU lógico(disjunção do rlm) - Só é False se tudo for False. Todos os outros são True
print(valor2 or valor2)

#not (igual a negação do rlm) - inverte o valor de uma variável
print(not valor1)
print(not valor2)

# == ou igualdade (utilizado para comparar dois valores. Se forem iguais, o resultado será True, caso contrário, será False)
print(valor1 == valor1)
print(valor1 == valor2)

#!= ou diferença ( utilizado para compara dois valores. Se forem diferntes, o resultado será True, caso contrário, será False)
print(valor1 != valor2)
print(valor1 != valor1)
