import sla

dic = {
    "1":sla.desafio_1,
    "2":sla.desafio_2,
}

escolha = input("Qual código quer rodar? ")

func = dic.get(escolha)

if func:
    func()
else:
    print("Função Não Encontrilda !!")