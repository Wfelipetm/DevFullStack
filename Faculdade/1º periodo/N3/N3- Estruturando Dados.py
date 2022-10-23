entrada_Conjunto = [1, 2, 3]
listThe_end = [[]]


def conjuntos(lista):
    for i in lista:
        listThe_end.append([i])
    for x in lista:
        for y in lista:
            if lista.index(y) >= lista.index(x) + 1:
                listThe_end.append([x, y])
    listThe_end.append(lista)

    return listThe_end


print(conjuntos(entrada_Conjunto))
