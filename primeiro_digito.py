def valida_primeiro_digito(CNPJ):
    multiplicadores = [5,4,'.',3,2,9,'.',8,7,6,'/',5,4,3,2]
    verificadores = CNPJ[0:15:1]
    acumulador = 0
    for index in range(0,len(verificadores)):
        if index == 2 or index == 6 or index == 10:
            continue
        else:
            acumulador = (multiplicadores[index]*verificadores[index])+acumulador

    digito = 11 - (acumulador % 11)
    if digito > 9:
        digito = 0
    else:
        digito = digito

    return digito



