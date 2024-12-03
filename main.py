from aluno_ensino_medio import AlunoEnsinoMedio
from aluno_graduacao import AlunoGraduacao
from professor import Professor

def verificar_aprovacao(aluno):
    try:
        media = aluno.calcular_media()
        aprovado = "Aprovado" if aluno.aprovado() else "Reprovado"
        return f"Aluno: {aluno.nome}, Matrícula: {aluno.matricula}, Média: {media:.2f}, Status: {aprovado}"
    except ValueError as e:
        return f"Erro: {e}"


aluno_ensino_medio = AlunoEnsinoMedio("João Silva", "12345")
aluno_ensino_medio.adicionar_nota(7)
aluno_ensino_medio.adicionar_nota(8)

aluno_graduacao = AlunoGraduacao("Maria Oliveira", "54321")
aluno_graduacao.adicionar_nota(6)
aluno_graduacao.adicionar_nota(5)

professor = Professor("Dr. Paulo Santos", "Doutorado")


print(verificar_aprovacao(aluno_ensino_medio))
print(verificar_aprovacao(aluno_graduacao))
print(professor.obter_informacoes())
