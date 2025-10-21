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
 
        if materia not in c[0]: 
            continue

        if nota < c[1]: #Se nota for menor que C
            continue #Ele continua

pts = nota
def participaçao(estudante):
    participaçao = estudante[3]
    if participacao > 0:
        if participacao > 10:
            pts += 15
        elif participacao > 5:
            pts += 10
        elif participacao > 2:
                pts += 5

def extra(estudante):
    trabalho_extra = estudante[4]
    if trabalho_extra:
        tipo_trabalho = trabalho_extra[0]
        nota_trabalho = trabalho_extra[1]
        if tipo_trabalho == 'projeto':
            if nota_trabalho > 80:
                pts += 20
            elif nota_trabalho > 60:
                pts += 15
            else:
                pts += 10
        elif tipo_trabalho == 'pesquisa':
            pts += nota_trabalho * 0.3        

        if b and i < len(b) and b[i]:
            bonus_tipo = b[i]
            if bonus_tipo == 'participacao':
                pts += 8
            elif bonus_tipo == 'excelencia':
                pts *= 1.3
            elif bonus_tipo == 'melhoria':
                pts *= 1.15

        if pts > 100:
            pts = 100

        if p[0] and nota < c[2]:
            if len(p) > 1 and p[1]:
                nota_recuperacao = min(nota + 20, c[1])
                pts = max(pts, nota_recuperacao)
            elif len(p) > 2 and p[2] and participacao > d:
                pts += 10

        total_pontos += pts

    nota_media = total_pontos / len(e)

    if nota_media > 95:
        nota_media = min(nota_media * 1.05, 100)
    elif nota_media > 85:
        nota_media = nota_media * 1.02

    return nota_media


if __name__ == "__main__":
    estudantes_teste = [
        [True, 'matematica', 75, 8, ['projeto', 85]],
        [True, 'fisica', 82, 12, ['pesquisa', 90]],
        [False, 'quimica', 60, 3, None],
        [True, 'matematica', 45, 15, ['projeto', 70]]
    ]

    config_teste = [['matematica', 'fisica', 'quimica'], 60, 50]

    politicas_teste = [True, True, True]

    bonus_teste = ['excelencia', 'melhoria', None, 'participacao']

    resultado = calcular_nota_estudante(
        estudantes_teste, config_teste, politicas_teste, bonus_teste)
    print(f"Nota média calculada: {resultado}")

    