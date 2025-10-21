# Problemas: Código repetitivo, falta de tratamento de exceções, validação inadequada, estrutura confusa

total_vendas = 0 
produto_mais_vendido = "" 
maior_quantidade = 0

# Produto 1
def cadastro_produto(nome_produto):
    while True:
        try:
            print("Cadastro Produto 1:") 
            nome_produto = input(f"O nome do produto é: {nome_produto} ") 
            if nome_produto == "" or nome_produto.isdigit():
                break
            print("\n\033 Nome inválido! Digite um Nome Válido! \n\033")
        except ValueError:
            print("\n\033 Entrada! Digite um nome que seja Válido! \n\033")
    return menu()

def cadastrar_preco(preco_produto):
    while True:
        try: 
            preco_produto = float(input(f"Preço unitário: R${preco_produto} ")) 
            if preco_produto >= 0:
                break 
            print("\n\033 Preço inválido! Ele deve ser MAIOR que ZERO! \n\033") 
        except ValueError:
            print("\n\033 Entrada Inválida! Digite um número para o Preço! \n\033")
    return menu()

def quantidade_vendida(qtd_vendida):
    while True:
        try:
            qtd_vendida = int(input(f"Quantidade vendida hoje foi de: {qtd_vendida} ")) 
            if qtd_vendida >= 0:
                break 
            print("\n\033 Quantidade inválida! Não pode ser NEGATIVA! \n\033")
        except ValueError:
            print("\n\033 Entrada Inválida! Digite um número para a Quantidade! \n\033")
    return menu()

def calcular_valores(preco_produto, qtd_vendida, total_vendas,):
    subtotal = preco_produto * qtd_vendida
    print(f"O Subtotal é: {subtotal}")
    total_vendas = total_vendas + subtotal
    print(f"O Total de Vendas foi de: {total_vendas}")
    return menu()


def resumo_dia(total_vendas_final, mais_vendido, qtd_mais_vendida): 
    print("\n Resumo do Dia: \n")
    print(f"Total de Vendas: R${total_vendas_final}")
    print(f"Produto mais Vendido: {mais_vendido} ({qtd_mais_vendida} unidades)")
    return menu()


def menu():
    print("\n Bem Vindo ao nosso Sistema de Vendas da Lanchonete \n")
    print("1. Cadastro do Produto")
    print("2. Cadastro do Preço")
    print("3. Quantidade Vendida")
    print("4. Calcular Valores")
    print("5. Resumo do Dia")
    print("6. Sair do Programa")
    opção = input("Escolha uma opção (1-6): ")
    if opção == '1':
        return cadastro_produto()
    elif opção == '2':
        return cadastrar_preco()
    elif opção == '3':
        return quantidade_vendida()
    elif opção == '4':
        return calcular_valores()
    elif opção == '5':
        return resumo_dia() 
    elif opção == '6':
        print ("\n\033[33m---Programa encerrado!---\033[0m")
        return True
    else:
        print("\n\033[31m Digite um Número entre 1 a 6! \033[0m")
        return False


while True:
    if menu():
        break