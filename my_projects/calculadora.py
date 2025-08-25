#Aqui está a definição para cada operação matemática desejada.
while True:
    print("Qual operação você deseja realizar?")
    print("S = Soma")
    print("SB = Subtração")
    print("M = Multiplicação")
    print("D = Divisão")
    print("R = Raiz Quadrada")
    print("SAIR = Encerrar o programa")

    operacao = input("Digite a operação correspondente: ")

    if operacao == 'SAIR':  
        print("Programa encerrado.")
        break

    if operacao == 'S':
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))
        print("Você escolheu Soma")

    elif operacao == 'SB':
        num1 = float(input("DIgite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))
        print("Você escolheu Subtração")

    elif operacao == 'M':
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))

        print("Você escolheu Multiplicação")

    elif operacao == 'D':
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))
        print("Você escolheu Divisão")

    elif operacao == 'R':
        num1 = float(input("Digite o primeiro número:"))
        print("Você escolheu Raiz Quadrada")

    else:
        print("Operação inválida pelo sistema. Escolha uma operação válida.")
        continue

    if operacao == 'S':
        resultado = num1 + num2
    elif operacao == 'SB':
        resultado = num1 - num2
    elif operacao == 'M':
        resultado = num1 * num2
    elif operacao == 'D':
        if num2 == 0:
            resultado = "Divisão por zero não é permitda"
        else:
            resultado = num1 / num2
    elif operacao == 'R':
        if num1 < 0:
            resultado = "Raiz quadrada de número negativo não é permitida"
        else:
            resultado = num1 ** 0.5

    if operacao in ['S', 'SB', 'M', 'D', 'R']:
        print(f"O resultado da operação {operacao} é: {resultado}")
    print("\n")  # Adiciona uma linha em branco para melhor legibilidade
    
    import time
    time.sleep(2.5)  # Pausa de 2.5 segundos para melhor visualização

    print("Continuando o programa...\n")  # Mensagem de continuação do programa