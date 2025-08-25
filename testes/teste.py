#lista = list(range(1, 100000, 2))
#print(lista)

#lista = [50, 20, 100, 80]
#def calcula_media(lista):
    #if len(lista) == 0:
        #return 0
    #return sum(lista) / len(lista)
#print(calcula_media(lista))



salarios = [1000, 2000, 400, 4500, 850]
funcionarios = ['João', 'Maria', 'José', 'Ana', 'Pedro']
for salario in salarios:
    if salario < 1000:
        print('Salário abaixo do mínimo')
    elif salario < 2000:
        print('Salário entre 1000 e 2000')
    elif salario < 3000:
        print('Salário entre 2000 e 3000')
    else:
        print('Salário acima de 3000')