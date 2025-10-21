# Problemas: Código repetitivo, falta de tratamento de exceções, validação inadequada, estrutura confusa

print("Sistema de Vendas - Lanchonete") #Printa a String

total_vendas = 0 #Defini total_vendas inicia 0
produto_mais_vendido = "" #Defini que recebe uma string fazia
maior_quantidade = 0 #Defini maior_quantidade inicia 0

# Produto 1
print("Cadastro Produto 1:") #Printa a String
nome_produto = input("Nome do produto: ") #Defini a variavel que recebe o nome do produto cadastrado
if nome_produto == "" or nome_produto.isdigit(): #Ela verifica se a string é vazia ou se ele é composta por digitos
    print("Nome inválido!") #Se for digitos ele printa a string
    nome_produto = "Produto Sem Nome" #Se o produto não foi cadastrado ele vai ficar com o nome de Produto Sem Nome

preco_produto = float(input("Preço unitário: R$ ")) #Defini uma variavel para o preço de um produto
if preco_produto <= 0: #Se o produto é menor que 0
    print("Preço inválido!") #Ele printa Preço Invalido
    preco_produto = 1.0 #Se o preço do produto não foi cadastrado ele fica como 1

qtd_vendida = int(input("Quantidade vendida hoje: ")) #Defini uma variavel para receber numeros
if qtd_vendida < 0: #Se for menor que 0
    print("Quantidade inválida!") #Ele printa Quantidade Invalida
    qtd_vendida = 0 #Se a quantidade não foi cadastrada ele fica como 0

subtotal = preco_produto * qtd_vendida #Subtotal vai ser o Preço do Produto vezes a Quantidade de Vendas
total_vendas = total_vendas + subtotal #Total de Vendas vai ser Total de Vendas mais o Subtotal
if qtd_vendida > maior_quantidade: #Se Quantidade de Vendas for maior que Maior Quantidade
    maior_quantidade = qtd_vendida #Maior Quantidade vai ser igual a Quantidade de Vendas
    produto_mais_vendido = nome_produto #Produto Mais Vendido vai ser igual a Nome do Produto

print(f"Produto: {nome_produto}") #Ele printa a string junto com a função
print(f"Preço: R$ {preco_produto}") #Ele printa a string junto com a função
print(f"Quantidade: {qtd_vendida}") #Ele printa a string junto com a função
print(f"Subtotal: R$ {subtotal}") #Ele printa a string junto com a função
print("-" * 30) #Printa 30 Hífen

# Produto 2
print("Cadastro Produto 2:")
nome_produto = input("Nome do produto: ")
if nome_produto == "" or nome_produto.isdigit():
    print("Nome inválido!")
    nome_produto = "Produto Sem Nome"

preco_produto = float(input("Preço unitário: R$ "))
if preco_produto <= 0:
    print("Preço inválido!")
    preco_produto = 1.0

qtd_vendida = int(input("Quantidade vendida hoje: "))
if qtd_vendida < 0:
    print("Quantidade inválida!")
    qtd_vendida = 0

subtotal = preco_produto * qtd_vendida
total_vendas = total_vendas + subtotal
if qtd_vendida > maior_quantidade:
    maior_quantidade = qtd_vendida
    produto_mais_vendido = nome_produto

print(f"Produto: {nome_produto}")
print(f"Preço: R$ {preco_produto}")
print(f"Quantidade: {qtd_vendida}")
print(f"Subtotal: R$ {subtotal}")
print("-" * 30)

# Produto 3
print("Cadastro Produto 3:")
nome_produto = input("Nome do produto: ")
if nome_produto == "" or nome_produto.isdigit():
    print("Nome inválido!")
    nome_produto = "Produto Sem Nome"

preco_produto = float(input("Preço unitário: R$ "))
if preco_produto <= 0:
    print("Preço inválido!")
    preco_produto = 1.0

qtd_vendida = int(input("Quantidade vendida hoje: "))
if qtd_vendida < 0:
    print("Quantidade inválida!")
    qtd_vendida = 0

subtotal = preco_produto * qtd_vendida
total_vendas = total_vendas + subtotal
if qtd_vendida > maior_quantidade:
    maior_quantidade = qtd_vendida
    produto_mais_vendido = nome_produto

print(f"Produto: {nome_produto}")
print(f"Preço: R$ {preco_produto}")
print(f"Quantidade: {qtd_vendida}")
print(f"Subtotal: R$ {subtotal}")
print("-" * 30)

# Produto 4
print("Cadastro Produto 4:")
nome_produto = input("Nome do produto: ")
if nome_produto == "" or nome_produto.isdigit():
    print("Nome inválido!")
    nome_produto = "Produto Sem Nome"

preco_produto = float(input("Preço unitário: R$ "))
if preco_produto <= 0:
    print("Preço inválido!")
    preco_produto = 1.0

qtd_vendida = int(input("Quantidade vendida hoje: "))
if qtd_vendida < 0:
    print("Quantidade inválida!")
    qtd_vendida = 0

subtotal = preco_produto * qtd_vendida
total_vendas = total_vendas + subtotal
if qtd_vendida > maior_quantidade:
    maior_quantidade = qtd_vendida
    produto_mais_vendido = nome_produto

print(f"Produto: {nome_produto}")
print(f"Preço: R$ {preco_produto}")
print(f"Quantidade: {qtd_vendida}")
print(f"Subtotal: R$ {subtotal}")
print("-" * 30)

print("RESUMO DO DIA:") #Printa a string
print(f"Total de vendas: R$ {total_vendas}") #Printa o Total de vendas e a função, com o valor em Reais
print(
    f"Produto mais vendido: {produto_mais_vendido} ({maior_quantidade} unidades)") #Printa qual foi o produto mais vendido e a maior quantidade em unidades