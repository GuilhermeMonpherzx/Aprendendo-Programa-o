def calcular_nota_estudante(e, c, p, b=None, d=5):
    """
    #Defini função calcular nota com parâmetros 
    # e = estudantes_teste
    # c = config_teste
    # p = politicas_teste
    # b = bonus_teste              None (Inicia como None/nada) 
    # d= 5 (Inicia d com 5)
    """
    if not e or len(e) == 0: #Se não tiver dentro da lista
        return 0 #Ele retorna 0

    total_pontos = 0 #Inicia a variavel total_pontos com 0

    for i in range(len(e)): #Para cada índice dentro do tamanho da lista
        estudante = e[i] #Defini o índice do estudante
        ativo = estudante[0] #Defini o índice para ativo
        materia = estudante[1] #Defini o índice para materia
        nota = estudante[2] #Defini o índice para nota
        participacao = estudante[3] #Defini o índice para participação
        trabalho_extra = estudante[4] if len(estudante) > 4 else None #Trabalho extra é igual a estudante na posição 4 e se o tamanho da lista Estudante for maior que 4 e se não for nada ele não vai ser nada

        if not ativo: #Se ele estiver ativo ele continua o codigo
            continue #BUG Explique a logica utiliza nesse condicional, e por que ele se comporta como ponto de parada para o sistema

        if materia not in c[0]: #Se materia não estiver dentro de C, ele para, senão
            continue #Ele continua

        if nota < c[1]: #Se nota for menor que C
            continue #Ele continua

        pts = nota #PTS é IGUAL a NOTA

        if participacao > 0: #Ele verifica se participação é maior que 0
            if participacao > 10: #Ele verifica se participação é maior que 0
                pts += 15 #Ele adiciona mais 15 pontos
            elif participacao > 5: #Ele verifica se participação é maior que 5
                pts += 10 #Ele adiciona mais 10 pontos
            elif participacao > 2: #Ele verifica se participação é maior que 2
                pts += 5 #Ele adiciona mais 5 pontos

        if trabalho_extra: 
            tipo_trabalho = trabalho_extra[0] #Defini tipo_trabalho é no índice 0 no trabalho_extra
            nota_trabalho = trabalho_extra[1] #Defini tipo_trabalho é no índice 1 no trabalho_extra

            if tipo_trabalho == 'projeto': #Se tipo_trabalho é igual ao valor do projeto
                if nota_trabalho > 80: #Ele verifica se nota_trabalho é maior que 80
                    pts += 20 #Se for ele adiciona mais 20
                elif nota_trabalho > 60: #Ele verifica se nota_trabalho é maior que 60
                    pts += 15 #Se for ele adiciona mais 15
                else:
                    pts += 10 #Se não for ele adiciona mais 10
            elif tipo_trabalho == 'pesquisa': #Se tipo_trabalho é igual ao valor do pesquisa
                pts += nota_trabalho * 0.3 #Ele pega o pontos e soma com a nota do trabalho e multiplica por 0.3

        if b and i < len(b) and b[i]:
            bonus_tipo = b[i] #bonus_tipo é a mesma b no índice que for dado
            if bonus_tipo == 'participacao': #Se bonus_tipo tem o mesmo valor que participação
                pts += 8 #Se ele for ele adiciona mais 8
            elif bonus_tipo == 'excelencia': #Se bonus_tipo tem o mesmo valor que excelencia
                pts *= 1.3 #Se ele for ele multiplica por 1.3
            elif bonus_tipo == 'melhoria': #Se bonus_tipo tem o mesmo valor que melhoria
                pts *= 1.15 #Se ele for ele multiplica por 1.15

        if pts > 100: #Se pts for maior que 100
            pts = 100 #Ele vai ser igual a 100

        if p[0] and nota < c[2]: #Se p no índice 0 que nota menor c no índice 2
            if len(p) > 1 and p[1]: #Ele verfica a lista de P e se for > que 1 e o p no índice 1
                nota_recuperacao = min(nota + 20, c[1]) #nota_recuperação ele vai tirar o min da nota, que a NOTA + 20, c no índice 1
                pts = max(pts, nota_recuperacao) #pts ele vai tirar o max dos pontos é os pts e nota_recuperação
            elif len(p) > 2 and p[2] and participacao > d: #Se não for ele lê a lista P maior and p índice 2 e participação maior que d
                pts += 10 #Se ele for ele adiciona mais 10

        total_pontos += pts #total_pontos soma com os pts

    nota_media = total_pontos / len(e) #nota_media é igual ao total_pontos e ele divide pela lista e

    if nota_media > 95: #Se nota_media for maior que 95
        nota_media = min(nota_media * 1.05, 100) #nota_media é o minimo que é nota_media vezes 1.05, e 100
    elif nota_media > 85: #Se nota_media for maior que 85
        nota_media = nota_media * 1.02 #Ele nota_media vai ser nota_media vezes 1.02

    return nota_media #Ele retorna nota_media


if __name__ == "__main__": #Ele verifica se o arquivo está sendo executado corretamente
    estudantes_teste = [
        [True, 'matematica', 75, 8, ['projeto', 85]],
        [True, 'fisica', 82, 12, ['pesquisa', 90]],
        [False, 'quimica', 60, 3, None],
        [True, 'matematica', 45, 15, ['projeto', 70]]
    ]

    config_teste = [['matematica', 'fisica', 'quimica'], 60, 50] #Aqui é a lista das matérias

    politicas_teste = [True, True, True] #Aqui se ele é Verdadeiro ou Falso

    bonus_teste = ['excelencia', 'melhoria', None, 'participacao'] #Aqui a lista do bônus teste

    resultado = calcular_nota_estudante(
        estudantes_teste, config_teste, politicas_teste, bonus_teste) #Aquie ele coloca ele cria uma váriavel
    print(f"Nota média calculada: {resultado}") #Printa a string junto com a função