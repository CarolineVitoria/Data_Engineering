import hashlib


def imprime_hashdigest():
    str = input("Digite sua entrada: ")
    str_encode = str.encode()
    saida = hashlib.sha1(str_encode).hexdigest()
    print(saida)
    resp = input("Deseja inserir mais um dado? s/n ")
    if resp.lower() == "s":
        imprime_hashdigest()
    else:
        return


imprime_hashdigest()
