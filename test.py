class conta():
    def __init__(self, __saldo,__numero,__agencia,__cliente,__historico):
        self.saldo = __saldo
        self.numero = __numero
        self.agencia = __agencia
        self.cliente = __cliente
        self.historico = __historico

    def saldo():
        return float

    def nova_conta(__numero , __cliente):
        return conta

    def sacar(valor):
        return bool

    def depositar(valor):
        return bool


class conta_corrente(conta):
    def __init__(self,__limite,__limite_saque):
        self.limite = __limite
        self.limite_saque = __limite_saque


class cliente():
    def __init__(self, __endereco, __contas):
        self.endereco = __endereco
        self.contas = __contas

    def realizar_transacao(conta, transacao):
        pass

    def adicionar_conta(conta):
        pass


class pessoa_fisica(cliente):
    def __init__(self, __cpf, __nome, __data_nascimento):
        self.cpf = __cpf
        self.nome = __nome
        self.data_nascimento = __data_nascimento


class transacao():
    def registrar(conta):
        pass


class historico():
    def adicionar_transacao(transacao):
        pass


class deposito():
    pass


class saqui():
    pass