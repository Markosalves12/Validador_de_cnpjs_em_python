def valida_segundo_digito(novo_CNPJ):
    multiplicadores = [6,5,'.',4,3,2,'.',9,8,7,'/',6,5,4,3,'-',2]
    verificadores = novo_CNPJ[:]
    acumulador = 0
    for index in range(0,len(verificadores)):
        if index == 2 or index == 6 or index == 10 or index == 15:
            continue
        else:
            acumulador = (multiplicadores[index]*verificadores[index])+acumulador

    digito = 11 - (acumulador % 11)
    if digito > 9:
        digito = 0
    else:
        digito = digito

    return digito

