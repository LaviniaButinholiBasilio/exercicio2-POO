from aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    def aprovado(self):
        media = self.calcular_media()
        return media >= 6
