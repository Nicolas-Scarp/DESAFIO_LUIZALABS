import sla

dic = {
    "1":sla.desafio_de_código_1,
    "2":sla.desafio_de_código_2,
    "3":sla.desafio_de_projeto_1,
    "4":sla.desafio_de_projeto_2,
}

escolha = input("Qual código quer rodar? ")

func = dic.get(escolha)

if func:
    func()
else:
    print("Função Não Encontrilda !!")