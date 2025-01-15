### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

# solicita que o usuário insira o seu nome
try:
    nome = input("Digite o seu primeito nome: ").upper()

    # verifica se nome está vazio
    if len(nome) == 0:
        raise ValueError("Nome não pode está vazio.")
# verifica se há número no nome
    elif any(char.isdigit() for char in nome):
        raise ValueError("Nome não pode conter número")
    else:
        print("Nome válido:", nome)
except ValueError as e:
    print(e)
    exit()

# Solicita o usuário que insira o seu salário e o converte para float
try:
    salario = float(input("Digite o seu salário: "))
    # verifica se o salário é menor que 0
    if salario < 0:
        print("Por favor, digite um valor positivo para o seu salário")
except ValueError:
    print("Entrada inválida par ao salário. Por favor, digite um número.")
    exit()

# Solicita ao usuário que insira o valor do bonus recebido e o converte para float
try:
    bonus = float(input("Digite o valor do seu bônus: "))
    # verifica se o salário é menor que 0
    if bonus < 0:
        print("Por favor, digite um valor positivo para o bônus")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")
    exit()

KPI = float(1000)

# calculo do salário mais o bônus
bonus_recebido = KPI + salario * bonus

# imprime a mensagem com o nome do usuário e o bônus a ser recebido
print(f"{nome}, seu salário é de {salario:.2f} e o bônus final é de {bonus_recebido:.2f}.")
