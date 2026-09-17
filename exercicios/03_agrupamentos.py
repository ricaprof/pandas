"""Exercícios de agrupamento e agregação (sem soluções)."""

from pathlib import Path

import pandas as pd


ARQUIVO = Path(__file__).resolve().parent.parent / "dados" / "vendas.csv"

# TODO 1: leia os dados e converta a coluna data para datetime.

# TODO 2: crie a coluna valor_bruto (quantidade * preco_unitario).

# TODO 3: crie a coluna valor_liquido aplicando o desconto percentual ao
# valor bruto.

# TODO 4: calcule o faturamento líquido total da empresa.

# TODO 5: encontre o faturamento e a quantidade de itens vendidos por filial.

# TODO 6: descubra qual vendedor teve o maior faturamento líquido.

# TODO 7: calcule, por categoria, faturamento, quantidade vendida e preço
# unitário médio usando uma única agregação.

# TODO 8: extraia mês e dia da semana da data e compare o faturamento entre
# esses períodos.

# TODO 9: crie uma tabela dinâmica com as filiais nas linhas, as categorias
# nas colunas e o faturamento líquido como valor. Preencha combinações ausentes
# com zero.

# TODO 10: descubra a forma de pagamento mais usada em número de transações e
# também a que movimentou o maior valor. Os resultados são iguais?

# TODO 11: selecione as 5 maiores vendas por valor líquido.

