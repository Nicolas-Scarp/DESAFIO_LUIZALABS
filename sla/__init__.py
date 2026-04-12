def desafio_1():
    entrada = input().strip(" ")
    preco_str, codigo_promocao = entrada.split()

    preco = float(preco_str)

    if codigo_promocao == "S":
        preco = preco - (preco * 0.10)
        print(f"{preco:.2f}")
    elif codigo_promocao == "N":
        '''eai, bão?'''
        print(f"{preco:.2f}")
    else:
        print("Código Não Encontrado!")


    