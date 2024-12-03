from aluno import Aluno

class AlunoGraduacao(Aluno):
    def aprovado(self):
        media = self.calcular_media()
        return media >= 7
