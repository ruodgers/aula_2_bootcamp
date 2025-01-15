# README - Desafio: Refatorar o Projeto da Aula Anterior Evitando Bugs

## Descrição

Este projeto tem como objetivo refatorar um programa que solicita informações ao usuário, como nome, salário e bônus, e calcula o bônus final. O foco principal é evitar bugs e melhorar a robustez do código.

## Funcionalidades

1. Solicita ao usuário que digite seu nome.
2. Solicita ao usuário que digite o valor do seu salário e converte a entrada para um número de ponto flutuante.
3. Solicita ao usuário que digite o valor do bônus recebido e converte a entrada para um número de ponto flutuante.
4. Calcula o valor do bônus final.
5. Imprime uma mensagem personalizada incluindo o nome do usuário, salário e bônus.

## Bugs e Riscos Identificados

Durante a análise do código, foram identificados os seguintes bugs e riscos:

1. **Nome Vazio**: O programa deve garantir que o nome não esteja vazio. Caso contrário, uma exceção é levantada.
2. **Números no Nome**: O programa deve verificar se o nome contém números, o que não é permitido.
3. **Salário Negativo**: O programa deve garantir que o salário informado seja um valor positivo.
4. **Bônus Negativo**: O programa deve garantir que o bônus informado seja um valor positivo.
5. **Entradas Inválidas**: O programa deve tratar entradas inválidas (não numéricas) para salário e bônus, evitando que o programa quebre.
6. **Cálculo do Bônus**: O cálculo do bônus final deve ser revisado para garantir que a lógica esteja correta.

## Estrutura do Código

O código é estruturado em blocos de `try-except` para capturar e tratar exceções. A seguir, uma breve descrição de cada parte:

- **Entrada do Nome**: O usuário é solicitado a inserir seu nome, que é validado para garantir que não esteja vazio e não contenha números.
- **Entrada do Salário**: O usuário é solicitado a inserir seu salário, que é convertido para um número de ponto flutuante e validado para garantir que seja positivo.
- **Entrada do Bônus**: O usuário é solicitado a inserir o valor do bônus, que também é convertido para um número de ponto flutuante e validado para garantir que seja positivo.
- **Cálculo do Bônus Final**: O bônus final é calculado com base no salário e no bônus informado.
- **Saída**: Uma mensagem personalizada é impressa, informando o usuário sobre seu salário e bônus final.

## Como Executar

Para executar o programa, siga os passos abaixo:

1. Certifique-se de ter o Python instalado em sua máquina.
2. Copie o código para um arquivo com a extensão `.py`. No caso em questão, o arquivo é denomidado `desafio_02.py`.
3. Execute o arquivo no terminal ou prompt de comando com o seguinte comando:
   ```bash
   python desafio_02.py

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias e correções.

