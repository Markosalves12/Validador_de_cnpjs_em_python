def separa_digitos(CNPJ):
    CNPJ_pos_filtro = list()
    for value in CNPJ:
        try:
            value = int(value)
            CNPJ_pos_filtro.append(value)
        except:
            if value == '.' or value == '/' or value == '-':
                CNPJ_pos_filtro.append(value)

    if len(CNPJ_pos_filtro) == 18:
            return CNPJ_pos_filtro
    else:
        print(f"Verifique o CNPJ digitado novamente")
        return False


def verifica_configuracao_cnpj(CNPJ_filtrado):
    if CNPJ_filtrado[2] != '.' or CNPJ_filtrado[6] != '.' or CNPJ_filtrado[10] != '/' or CNPJ_filtrado[15] != '-':
        print('Ha algo errado com o CNPJ digitado')
        return False
    else:
        return True




