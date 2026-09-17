"""Exercícios de fundamentos do pandas (sem soluções)."""

from pathlib import Path

import pandas as pd


ARQUIVO = Path(__file__).resolve().parent.parent / "dados" / "alunos.csv"

# TODO 1: leia o arquivo CSV e armazene o resultado em um DataFrame.

# TODO 2: mostre as 5 primeiras e as 5 últimas linhas.

# TODO 3: descubra o número de linhas, o número de colunas e os tipos dos dados.

# TODO 4: selecione somente as colunas aluno, turma, nota_1 e nota_2.

# TODO 5: filtre os alunos da turma B.

# TODO 6: filtre os alunos que tiveram menos de 5 faltas e nota_1 maior ou
# igual a 7.

# TODO 7: crie a coluna media com a média aritmética de nota_1 e nota_2.

# TODO 8: ordene os alunos da maior para a menor média. Em caso de empate,
# ordene pelo nome em ordem alfabética.

# TODO 9: encontre a maior nota_2, a menor nota_2 e a média geral dessa prova.

# TODO 10: conte quantos alunos pertencem a cada turma.

# TODO 11: crie a coluna situacao usando estas regras:
# - média maior ou igual a 7 e até 7 faltas: "Aprovado"
# - caso contrário: "Reprovado"

# TODO 12: exiba apenas os alunos aprovados, mostrando nome, média e situação.

