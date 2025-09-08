#Grupo: Guilherme Broccolo Monteiro-INFA
import time # importa a biblioteca de TIME
salario = 0 #Define o salário inicial igual a 0
gastos = [] #Abro a lista chamada GASTOS

def adicionar_salario(): #Defini a função Adicionar Salário
    global salario #Aqui ele coloca a variável SALARIO, global para ela por ser chamada em qualquer função
    while True: #Aqui ele cria um loop infinito
        try: #Aqui ele tenta transformar o que foi digitado em número decimal por causa do FLOAT 
            salario = float(input("Digite o valor do seu salário mensal: R$")) #Defini uma variável e ele poder receber números quebrados e inteiros, mostra a string
            if salario > 0:
                print(f"\n\033[32mA Salário de R$ {salario:.2f}  foi registrado com sucesso. \033[0m") #Depois de ter passado pela verificação ele printa que foi registrado
            else:
                print("\n\033[31mSalário não pode ser  ZERO ou NEGATIVO!\n\033[0m") #Aqui ele printa a string 
            break  #Se ele não deu erro o break faz o loop parar, se não ele continua o loop
        except ValueError: #Ele verificar se foi digitado só números, se você colocar  um número ele da certo, se for letra ai ele da erro
            print("\033[31mDigite apenas números!\033[0m") #Ele vai printar na tela para digitar apenas números  
    return menu() #Ele retorna para o menu
def adicionar_gasto_mensal(): #Defini a função Adicionar Gasto Mensal
    while True: #Cria o loop infinito
        try: #Ele tenta transformar o que foi digitado para número decimal
            gastomensal = float(input("Digite o valor do seu gasto mensal: R$"))#Defini uma uma variável para receber números(INT ou FLOAT), e mostra a string
            if gastomensal > 0:
                print(f"\n\033[32mA Salário de R$ {gastomensal:.2f}  foi registrado com sucesso. \033[0m") #Depois de ter passado pela verificação ele printa que foi registrado
            else:
                print("\n\033[31mSalário não pode ser NEGATIVO!\n\033[0m") #Printa a string
            break #Se ele não deu erro, ele para o loop, mas se não, ele continua o loop
        except ValueError: #Ele vê se foi digitado algo diferente de número, ele vai aparecer para digitar apenas números, mas se digitou certo, ele não aparece
            print("\033[31mDigite apenas números!\033[0m") #Ele printa a string
    return menu() #Retorna para o menu novamente

def adicionar_gasto_categoria():  # Defini uma função Adicionar Gasto por Categoria
    print("Selecione o tipo de categoria:")  # Mostra as opções por categoria
    print("1. Alimentação")  # opção 1
    print("2. Transporte")  # opção 2
    print("3. Lazer")  # opção 3
    print("4. Saúde")  # opção 4
    print("5. Outros")  # opção 5

    categoria_opcao = input("Escolha uma categoria (1-5): ")  # Lê a escolha do usuário como string

    categorias = {  # Ele mapeia as categorias
        '1': 'Alimentação',
        '2': 'Transporte',
        '3': 'Lazer',
        '4': 'Saúde',
        '5': 'Outros'
    }

    if categoria_opcao in categorias:  # Ele valida se a opção existe
        if categoria_opcao == '5':  # Caso seja "Outros"
            categoria_escolhida = input("Digite o nome para especificar a categoria: ")  # Pede para especificar a categoria
        else:
            categoria_escolhida = categorias[categoria_opcao]  # Pega a categoria pelo dicionário

        try:
            valor = float(input(f"Digite o valor do gasto em {categoria_escolhida}: R$ "))  # Recebe o valor do gasto

            if valor <= 0:  # Impede valores negativos ou zero
                print("\n\033[31mO valor do gasto não pode ser ZERO ou NEGATIVO!\n\033[0m") #Printa a string
                return adicionar_gasto_categoria()  # Retorna para a função se o valor for inválido

            gastos.append((categoria_escolhida, valor))  # Salva o nome da categoria e o valor dentro da lista
            print(f"\n\033[32mGasto de R$ {valor:.2f} em {categoria_escolhida} adicionado. \033[0m")  # Mostra mensagem de sucesso
            print(gastos)  # Só para debug, pode remover depois

        except ValueError:  # Se tiver algo diferente de número ele vai dar erro
            print("\n\033[31mDigite apenas números para o gasto!\033[0m")  # Mostra a mensagem de erro
            return adicionar_gasto_categoria()  # Retorna em Adicionar Gasto por Categoria

        return menu()  # Retorna para o menu
    else:
        print("\n\033[31m-----Digite um número Válido!-----\033[0m")  # Mensagem caso a opção seja inválida
        return adicionar_gasto_categoria()  # Retorna em Adicionar Gasto por Categoria




def ver_relatorio(): #Defini a função Ver Relatório
    print("\n\033[36mAnalisando os gastos...\033[0m") #Printa Analisando os gastos
    time.sleep(1) #Adiciona um delay

    if not gastos: #Se não tiver nada dentro de Gastos
        print("\n\033[31mNenhum Gasto Registrado! \033[0m") #Ele printa Nenhum Gasto Registrado
        return menu() #Retorna no menu
    else:
        print("\n-----Relatório de Gastos-----") #Printa Relatório de Gastos
        if not salario: #Se não tiver nada dentro de Salário
            print("Nenhum Salário Registrado!") #Ele printa Nenhum Salário Registrado
        else:
            print(f"Sálario: {salario:.2f}") #Printa a variável salário
        total_gastos = 0 #defini o total de gastos para 0
        for  categoria, valor in gastos: #Ele percorre a lista de categoria, valor e gasto
            print(f"{categoria}: R$ {valor:.2f}") #Printa a categoria e o valor dela
            total_gastos += valor #Total de gasto é definido como maior ou igual ao valor
        print(f"\nTotal de Gastos: R$ {total_gastos:.2f}") #Printa o Total dos Gastos
        if salario > 0: #Se salário for maior que 0
            saldo = salario - total_gastos # Saldo vai ser o salário menos o Total de Gastos
            print(f"Saldo após Gastos: R$ {saldo:.2f}") #Printa o saldo após os Gastos
        else:
            print("Salário não registrado.") #Se não tiver nenhum salário registrado ele printa que não tem nenhum salário
        return menu() #Retorna para o menu

def menu(): #Defini a função Menu
    print("\n", 10*" =", "\n   Controle de Gastos Pessoais:", "\n", 10*" =") #Printa Controle de Gastos
    print("1. Registrar Salário Mensal") #Printa a opção Registrar Salário Mensal
    print("2. Adicionar Gastos Mensais") #Printa a opção Adicionar Gastos Mensais
    print("3. Adicionar Gastos por Categoria") #Printa a opção Adicionar Gastos por Categoria
    print("4. Ver Relatório de Gastos") #Printa a opção Ver Relatório de Gastos
    print("5. Encerrar Programa") #Printa a opção Encerrar Programa
    opção = input("Escolha uma opção (1-5):") # Defini a variável e mostra a string, e depois escolhe a opção
    if opção == '1': #Se for a opção 1 ele vai retornar para a primeira função
        return adicionar_salario()
    elif opção == '2': #Se for a opção 2 ele vai retornar para a segunda função
        return adicionar_gasto_mensal()
    elif opção == '3': #Se for a opção 3 ele vai retornar para a terceira função
        return adicionar_gasto_categoria()
    elif opção == '4': #Se for a opção 4 ele vai retornar para a quarta função
        return ver_relatorio()
    elif opção == '5': #Se for a opção 5 ele vai retornar para a quinta função
        time.sleep(1) #Ele adicionar um delay
        print ("\n\033[33m---Programa encerrado!---\033[0m") #Printa a string
        return True
    else:
        print("\n\033[31m---Digite um Número entre 1 a 5!---\033[0m") #Printa a string
        return False
while True:#Aqui vai fazer o programa terminar
    if menu():
        break