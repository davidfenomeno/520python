def encontra_impares(lista):
    lis = []
    if len(lista) == 1 and lista[0] % 2 == 0:
        if not lista[0] % 2 == 0:
            return lis
        return lista
    else:
        if lista[0] % 2 == 0:
            return lista[0] + encontra_impares(lista[1:])