import time
salario = 0
gastos = []

def adicionar_salario():
    global salario
    while True:
        try:
            salario = float(input("Digite o valor do seu salário mensal: R$"))
            break
        except ValueError:
            print("\033[31mDigite apenas números!\033[0m")
    print(f"\n\033[32mA Salário de R$ {salario:.2f} registrado com sucesso. \033[0m")
    return menu()

def adicionar_gasto_mensal():
    while True:
        try:
            gastomensal = float(input("Digite o valor do seu gasto mensal: R$"))
            break
        except ValueError:
            print("\033[31mDigite apenas números!\033[0m")
    print(f"\n\033[32mA Gasto mensal é de R$ {gastomensal:.2f} adicionado. \033[0m")
    return menu()

def adicionar_gasto_categoria():
    print("Selecione o tipo de categoria:")
    print("1. Alimentação")
    print("2. Transporte")
    print("3. Lazer")
    print("4. Saúde")
    print("5. Outros")
    categoria_opção = input("Escolha uma categoria (1-5): ")
    categorias = {
        '1': 'Alimentação',
        '2': 'Transporte',
        '3': 'Lazer',
        '4': 'Saúde',
        '5': 'Outros'
    }
    if categoria_opção in categorias:
        valor =float(input(f"Digite o valor do gasto em {categorias[categoria_opção]}: R$ "))
        gastos.append((categorias[categoria_opção], valor))
        print(f"\n\033[32mGasto de R$ {valor:.2f} em {categorias[categoria_opção]} adicionado. \033[0m")
        print(gastos)
        return menu()
    else:
        print("\n\033[31m-----Digite um número Válido!-----\033[0m")
        return adicionar_gasto_categoria()

def ver_relatorio():
    print("\n\033[36mAnalisando os gastos...\033[0m")
    time.sleep(1)

    if not gastos:
        print("\n\033[31mNenhum Gasto Registrado! \033[0m")
        return menu()
    else:
        print("\n-----Relatório de Gastos-----")
        if not salario:
            print("Nenhum Salário Registrado!")
        else:
            print(f"Sálario: {salario:.2f}")
        total_gastos = 0
        for  categoria, valor in gastos:
            print(f"{categoria}: R$ {valor:.2f}")
            total_gastos += valor
        print(f"\nTotal de Gastos: R$ {total_gastos:.2f}")
        if salario > 0:
            saldo = salario - total_gastos
            print(f"Saldo após Gastos: R$ {saldo:.2f}")
        else:
            print("Salário não registrado.")
        return menu()

def menu():
    print("\n", 10*" =", "\n   Controle de Gastos Pessoais:", "\n", 10*" =")
    print("1. Registrar Salário Mensal")
    print("2. Adicionar Gastos Mensais")
    print("3. Adicionar Gastos por Categoria")
    print("4. Ver Relatório de Gastos")
    print("5. Ver Média dos Gastos")
    print("6. Encerrar Programa")
    opção = input("Escolha uma opção (1-5):")
    if opção == '1':
        return adicionar_salario()
    elif opção == '2':
        return adicionar_gasto_mensal()
    elif opção == '3':
        return adicionar_gasto_categoria()
    elif opção == '4':
        return ver_relatorio()
    elif opção == '5':
        time.sleep(1)
        print ("\n\033[33m---Programa encerrado!---\033[0m")
        return True
    else:
        print("\n\033[31m---Digite um Número entre 1 a 5!---\033[0m")
        return False
while True:
    if menu():
        break