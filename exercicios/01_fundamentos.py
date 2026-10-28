"""Exercícios de fundamentos do pandas (sem soluções)."""

from pathlib import Path

import pandas as pd


ARQUIVO = Path(__file__).resolve().parent.parent / "dados" / "alunos.csv"

# TODO 1: leia o arquivo CSV e armazene o resultado em um DataFrame.
df = pd.read_csv(ARQUIVO, sep=",")

# TODO 2: mostre as 5 primeiras e as 5 últimas linhas.
print(df.head(5))  # Exibe as 5 primeiras linhas
print(df.tail(5))  # Exibe as 5 últimas linhas

# TODO 3: descubra o número de linhas, o número de colunas e os tipos dos dados.
print(f"Número de linhas: {df.shape[0]}")
print(f"Número de colunas: {df.shape[1]}")
print(f"Tipos dos dados:\n{df.dtypes}")

# TODO 4: selecione somente as colunas aluno, turma, nota_1 e nota_2.
df_selecionado = df[["nota_1", "nota_2", "aluno", "turma"]]

# TODO 5: filtre os alunos da turma B.
df_turma_b = df[df["turma"] == "B"]

# TODO 6: filtre os alunos que tiveram menos de 5 faltas e nota_1 maior ou
# igual a 7.
df_filtrado = df[df['faltas'] < 5]
df_filtrado = df_filtrado[df['nota_1'] >= 7]
#df_filtrado = df[(df['faltas'] < 5) & (df['nota_1'] >= 7)]
print(df_filtrado.head())

df_filtrado = df[(df['faltas'] < 5) &  df['nota_1']  >= 7 ] 

# TODO 7: crie a coluna media com a média aritmética de nota_1 e nota_2.
df["media"] = (df['nota_1'] + df['nota_2']) / 2 
df['media'] = df['media'].round(2)
print(df.head(2))

# TODO 8: ordene os alunos da maior para a menor média. Em caso de empate,
# ordene pelo nome em ordem alfabética.
df_sort = df.sort_values(by='media') # Crescente
df_sort = df.sort_values(by=['media', 'aluno'], ascending=[False, True])
print(df_sort.head(15))



# TODO 9: encontre a maior nota_2, a menor nota_2 e a média geral dessa prova.
df_maior_nota = df['nota_2'].max()
df_menor_nota = df['nota_1'].min()
df_media_geral = df['nota_2'].mean()
print(df_media_geral)

# TODO 10: conte quantos alunos pertencem a cada turma.
df_quantidade = df['turma'].value_counts()
print(df_quantidade)


# TODO 11: crie a coluna situacao usando estas regras:
# - média maior ou igual a 7 e até 7 faltas: "Aprovado"
# - caso contrário: "Reprovado"

#comentario novo

#Primeiro reprova todos
df['situacao'] = "Reprovado"
condicao = ((df['media'] >=  7 ) & ( df['faltas'] <= 7))

print(f"condicao: {condicao}")
df.loc[condicao, 'situacao' ] = 'Aprovado'

print(df.head(15))

# TODO 12: exiba apenas os alunos aprovados, mostrando nome, média e situação.

condicao = df['situacao'] == "Aprovado"

df_aprovado = df[condicao]

print(df_aprovado.head(10))

df_aprovado = df_aprovado[['aluno', 'media', 'situacao']]

df_aprovado.to_csv("resposta/alunos_aprovados.csv")


df_aprovado = df[df['situacao'] == "Aprovado"]

print(df_aprovado.head(10))

df_aprovado.to_excel("resposta/alunos_aprovados.xlsx", index=False)

