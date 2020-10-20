class ContaBancaria:
    def __init__(self, titular, agencia, conta, saldo):
        self.titular = titular
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def obter_saldo(self):
        return self.saldo

    def creditar_valor(self, valor):
        self.saldo += valor
        return self.saldo

    def debitar_valor(self, valor):
        self.saldo -= valor
        return self.saldo

    def transferir_valor(self, conta_destino, valor):
        self.saldo -= valor
        conta_destino.saldo += valor


class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, agencia, conta, saldo, dia_aniversario):
        super().__init__(titular, agencia, conta, saldo)
        self.dia_aniversario = dia_aniversario

    def render(self, dia, taxa):
        #  Se o dia for igual ao dia do aniversário da caderneta de poupança, então:
        if dia == self.dia_aniversario:
            self.saldo += (taxa * self.saldo / 100.0)
        return self.saldo


class ContaCorrente(ContaBancaria):
    def __init__(self, titular, agencia, conta, saldo, pacote_servico):
        super().__init__(titular, agencia, conta, saldo)
        self.pacote_servico = pacote_servico

    def descontar_taxa_mensal(self):
        if self.pacote_servico == 'Estudante':
            self.saldo -= 10
        elif self.pacote_servico == 'Comum':
            self.saldo -= 20
        elif self.pacote_servico == 'Executivo':
            self.saldo -= 50
        else:
            self.saldo -= 15
