def maiores_que_media(conteudo:dict)->list:

    media_precos = sum(conteudo.values()) / len(conteudo)

    produtos_acima_media = [(produto, preco) for produto, preco in conteudo.items() if preco > media_precos]

    produtos_ordenados = sorted(produtos_acima_media, key=lambda x: x[1])

    return produtos_ordenados
