"""Exercícios de agrupamento e agregação (sem soluções)."""

from pathlib import Path

import pandas as pd


ARQUIVO = Path(__file__).resolve().parent.parent / "dados" / "vendas.csv"

# TODO 1: leia os dados e converta a coluna data para datetime.
df = pd.read_csv(ARQUIVO)
df['data'] = pd.to_datetime(
    df["data"],
    errors="coerce",
    format="mixed",
    dayfirst=True
)

# TODO 2: crie a coluna valor_bruto (quantidade * preco_unitario).
df["valor_bruto"] = df["quantidade"] * df["preco_unitario"]


# TODO 3: crie a coluna valor_liquido aplicando o desconto percentual ao
# valor bruto.

df["valor_liquido"] = df["valor_bruto"] * df["desconto_percentual"]

# TODO 4: calcule o faturamento líquido total da empresa.
faturamento_liquido = df['valor_liquido'].sum()
#print(faturamento_liquido)

# TODO 5: encontre o faturamento e a quantidade de itens vendidos por filial.
item_por_filial = df.groupby("filial")[['valor_liquido', 'quantidade']].sum()
print(item_por_filial)

# TODO 6: descubra qual vendedor teve o maior faturamento líquido.
vendas_por_vendedor = df.groupby("vendedor")["valor_liquido"].sum()
maior_vendedor = vendas_por_vendedor.idxmax()
print(maior_vendedor) 
print(vendas_por_vendedor[maior_vendedor])

# TODO 7: calcule, por categoria, faturamento, quantidade vendida e preço
# unitário médio usando uma única agregação.
a = df.groupby("categoria")[["faturamento", "quantidade", "preco", "valor_liquido"]].sum()

# TODO 8: extraia mês e dia da semana da data e compare o faturamento entre
# esses períodos.

# TODO 9: crie uma tabela dinâmica com as filiais nas linhas, as categorias
# nas colunas e o faturamento líquido como valor. Preencha combinações ausentes
# com zero.

# TODO 10: descubra a forma de pagamento mais usada em número de transações e
# também a que movimentou o maior valor. Os resultados são iguais?

# TODO 11: selecione as 5 maiores vendas por valor líquido.

