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
df["valor_liquido"] = df["valor_bruto"] * (1 - df["desconto_percentual"] / 100)

# TODO 4: calcule o faturamento líquido total da empresa.
faturamento_liquido = df['valor_liquido'].sum()
print(f"Faturamento líquido total: R$ {faturamento_liquido:.2f}")

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
vendas_por_categoria = df.groupby("categoria").agg(
    faturamento_liquido=("valor_liquido", "sum"),
    quantidade_vendida=("quantidade", "sum"),
    preco_unitario_medio=("preco_unitario", "mean")
)
print(vendas_por_categoria)

# TODO 8: extraia mês e dia da semana da data e compare o faturamento entre
# esses períodos.
df["mes"] = df["data"].dt.month
df["dia_semana"] = df["data"].dt.day_name()
faturamento_por_mes = df.groupby("mes")["valor_liquido"].sum()
faturamento_por_dia = df.groupby("dia_semana")["valor_liquido"].sum()
print("Faturamento por mês:")
print(faturamento_por_mes)
print("Faturamento por dia da semana:")
print(faturamento_por_dia)

# TODO 9: crie uma tabela dinâmica com as filiais nas linhas, as categorias
# nas colunas e o faturamento líquido como valor. Preencha combinações ausentes
# com zero.
tabela_dinamica = pd.pivot_table(
    df,
    index="filial",
    columns="categoria",
    values="valor_liquido",
    aggfunc="sum",
    fill_value=0
)
print(tabela_dinamica)

# TODO 10: descubra a forma de pagamento mais usada em número de transações e
# também a que movimentou o maior valor. Os resultados são iguais?
transacoes_por_pagamento = df["forma_pagamento"].value_counts()
faturamento_por_pagamento = df.groupby("forma_pagamento")["valor_liquido"].sum()
forma_mais_usada = transacoes_por_pagamento.idxmax()
forma_maior_faturamento = faturamento_por_pagamento.idxmax()
print(f"Forma de pagamento mais usada: {forma_mais_usada}")
print(f"Forma de pagamento com maior faturamento: {forma_maior_faturamento}")
print(f"Os resultados são iguais? {forma_mais_usada == forma_maior_faturamento}")

# TODO 11: selecione as 5 maiores vendas por valor líquido.
cinco_maiores_vendas = df.nlargest(5, "valor_liquido")
print(cinco_maiores_vendas[["venda_id", "filial", "vendedor", "valor_liquido"]])

