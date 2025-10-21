def processar_dados_cliente(clientes, configuracoes, opcoes): #Definimos uma função com os parâmetros CLIENTES, CONFIGURAÇOES E OPÇOES
    resultados = [] #Definimos uma lista
    for i, cliente in enumerate(clientes): #Ele percorre a lista e vai mostrar em que índice ela está
        if cliente[0]:  #Se cliente for 0 ele está ativo
            if cliente[1] == 'premium': #Se cliente for 1 ele está ativo como PREMIUM
                for produto in cliente[4]: #Ele percorre a lista de produto dentro de cliente e mostra o produto
                    if produto[0] in configuracoes[0]: #Ele verifica que o nome da categoria produto está dentro de configuraçoes
                        if produto[1] > configuracoes[1]: #Ele verifica se o nome da categoria produto é maior que de configuraçoes
                            if opcoes[0]: #Ele verifica se tem algo em opçoes
                                desconto = 0 #Inicia o Desconto com 0
                                if cliente[2] > 5: #Se cliente começa no índice 2 e se é maior que 5
                                    desconto = 0.2 #Definiu o desconto pra 0.2
                                elif cliente[2] > 3: #Se cliente começa no índice 2 e se é maior que 3
                                    desconto = 0.15 #Definiu o desconto pra 0.15
                                elif cliente[2] > 1: #Se cliente começa no índice 2 e se é maior que 1
                                    desconto = 0.1 #Definiu o desconto pra 0.1
                                else:
                                    if cliente[3] > 10: #Se cliente começa no índice 3 e se é maior que 10
                                        desconto = 0.05 #Desconto vai ser 0.05
                                produto[2] = produto[1] * \
                                    (1 - desconto) #Aqui ele tira o desconto - 1
                            resultados.append(produto) #Ele adiciona o valor em Produto
                    elif opcoes[1] and i % 2 == 0: #Ele divide o índice por 10 até ter resto igual a 0
                        resultados.append(produto) #Ele adiciona o valor em Produto
    return resultados #Retorna em Resultados


if __name__ == "__main__": #Aqui ele verifica se o arquivo está sendo executado
    clientes_teste = [ #Definimos uma lista
        [
            True,
            'premium',
            6,
            15,
            [
                ['eletronicos', 1000, None],
                ['livros', 50, None]
            ]
        ]
    ]

    configuracoes_teste = [ #Definimos outra lista
        ['eletronicos', 'casa'],
        500
    ]

    opcoes_teste = [ #Definimos novamente outra lista
        True,
        False
    ]

    resultado = processar_dados_cliente( 
        clientes_teste, configuracoes_teste, opcoes_teste)#Defini que resultado é igual a processar_dados_cliente com os parâmetros clientes_teste, configuraçoes_teste, opçao_teste
    print("Resultado do teste:") #Printa a string
    print(resultado) #Printa a variável resultado