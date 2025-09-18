import time
lista_compras = []

def adicionar_item():
    while True:
        try:
            nome = input("Digite o nome do item para a Lista:").strip()
            quantidade = int(input("Digite a quantidade do Item:"))
            preço = float(input("Digite o preço do Item: R$ "))
            
            if quantidade <= 0 or preço <= 0:
                print("\n\033[31mQuantidade e preço devem ser maiores que ZERO!\n\033[0m")
                return
            
            lista_compras.append((nome, quantidade, preço))
            print(f"\n {quantidade} X {preço} adicionado por R$ {preço:.2f} cada. \n")

        except ValueError:
            print("\n\033[32mDigite números válidos para Quantidade e Preço!\n\033[0m")

def 