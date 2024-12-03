from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            raise ValueError("Nota deve estar entre 0 e 10")

    def calcular_media(self):
        if not self.notas:
            raise ValueError(f"Aluno {self.nome} ainda não tem notas registradas.")
        return sum(self.notas) / len(self.notas)

    def aprovado(self):
        raise NotImplementedError("Método aprovado não implementado")
