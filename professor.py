from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, titulacao):
        super().__init__(nome)
        self.titulacao = titulacao

    def obter_informacoes(self):
        return f"Professor {self.nome}, Titulação: {self.titulacao}"
