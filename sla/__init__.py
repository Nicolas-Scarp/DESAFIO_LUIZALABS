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

def desafio_2():
    produtos = input().strip().split()

    contador=0
    soma_items=[]
    while contador < len(produtos):
        quantidade = produtos.count(produtos[contador])
        soma_items.append(quantidade)
        contador += 1

    maior_valor=max(soma_items)
    indice = soma_items.index(maior_valor)

    produto=produtos[indice]

    print(produto)
  
    