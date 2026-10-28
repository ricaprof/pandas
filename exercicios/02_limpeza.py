"""Exercícios de limpeza e preparação de dados (sem soluções)."""

from pathlib import Path

import pandas as pd


ARQUIVO = Path(__file__).resolve().parent.parent / "dados" / "clientes_sujos.csv"

# TODO 1: carregue o dataset e faça uma inspeção inicial (linhas, colunas,
# tipos e quantidade de valores ausentes por coluna).
df = pd.read_csv(ARQUIVO)
print(df.shape[0])
print(df.shape[1])
print(df.dtypes)

df_original = df.copy()


# TODO 2: identifique as linhas completamente duplicadas e remova as cópias.
df_sem_duplicata = df.duplicated(keep="last")
print(df[df_sem_duplicata]) #Mostra quais são as linhas duplicadas
df_novo = df.drop_duplicates()
print(df_novo.head(15))

# TODO 3: verifique se existem IDs repetidos com informações diferentes.
# Mantenha apenas um registro por cliente e anote em um comentário o critério
# que você escolheu para decidir qual registro preservar.
df_id_repetido = df.duplicated(subset="cliente_id", keep="first") #Mantém apenas o primeiro registro
print(df[df_id_repetido])
df.drop_duplicates(subset="cliente_id", keep="first", inplace=True)




# TODO 4: remova espaços extras no começo e no fim dos nomes.
df["nome"] = df["nome"].str.strip()
#df.to_csv("teste.csv") #usei para testar se funcionou

# TODO 5: padronize os nomes das cidades (há diferenças de maiúsculas,
# minúsculas, acentos e espaços).

#Critério -> Colocar tudo para minúscula
df["cidade"] = df["cidade"].str.strip().str.lower()
#print(df)

dict = {"são paulo": "sao paulo"}

df["cidade"] = df["cidade"].replace(dict)

# TODO 6: converta a coluna data_cadastro para datetime. Alguns registros
# possuem formatos diferentes e um deles é inválido.
df["data_cadastro"] = pd.to_datetime(
    df["data_cadastro"],
    format="mixed", #formatos diferentes
    dayfirst=True, #Tentar sempre colocar dia primeiro
    errors="coerce" #COlocar como NaT
)
print(df)

# TODO 7: converta renda_mensal para número. Trate os valores que não puderem
# ser convertidos e escolha uma estratégia para os valores ausentes.

#Vamos usar a média para resolver valores ausentes

df["renda_mensal"] = pd.to_numeric(
    df["renda_mensal"],
    errors="coerce"
)

media = df["renda_mensal"].mean().round(2)

df["renda_mensal"] = df["renda_mensal"].fillna(media)

print(df["renda_mensal"])

# TODO 8: padronize os e-mails em letras minúsculas e identifique endereços
# que não contêm o caractere @.

df["email"] = df["email"].str.lower()
df = df[df["email"].str.contains("@", na=False)]
print(df)




# TODO 9: padronize a coluna ativo para conter somente os valores booleanos
# True e False.
df["ativo"] =  df["ativo"].str.lower()

valores = {
    'sim': True,
    's': True,
    'true': True,
    'não': False,
    'nao': False,
    'n': False,
    'false': False,
    '0': False
}




df["ativo"] = df["ativo"].map(valores)
print(df)
print(df.dtypes)



# TODO 10: crie um relatório simples com a quantidade de problemas encontrados
# em cada coluna antes da limpeza.

# TODO 10: relatório de problemas encontrados antes da limpeza.

relatorio = {
    "duplicatas_completas": df_original.duplicated().sum(),
    "ids_duplicados": df_original.duplicated(subset="cliente_id").sum(),
    "nomes_com_espacos": (
        df_original["nome"] != df_original["nome"].str.strip()
    ).sum(),
    "datas_invalidas": pd.to_datetime(
        df_original["data_cadastro"],
        format="mixed",
        dayfirst=True,
        errors="coerce"
    ).isna().sum(),
    "rendas_invalidas": pd.to_numeric(
        df_original["renda_mensal"],
        errors="coerce"
    ).isna().sum(),
    "emails_invalidos": (
        ~df_original["email"].str.contains("@", na=False)
    ).sum()
}

print(relatorio)



# TODO 11: salve o DataFrame limpo como dados/clientes_limpos.csv sem gravar
# o índice do pandas.

df.to_csv("resposta/clientes_limpos.csv", index=False)