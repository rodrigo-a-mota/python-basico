from pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self, nome, cpf, idade):
        Pessoa.__init__(self, nome, cpf, idade)
