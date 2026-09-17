"""Exercícios de junção de DataFrames (sem soluções)."""

from pathlib import Path

import pandas as pd


PASTA_DADOS = Path(__file__).resolve().parent.parent / "dados"
ARQUIVO_CLIENTES = PASTA_DADOS / "clientes_loja.csv"
ARQUIVO_PRODUTOS = PASTA_DADOS / "produtos.csv"
ARQUIVO_PEDIDOS = PASTA_DADOS / "pedidos.csv"

# TODO 1: leia os três arquivos em DataFrames separados e inspecione suas
# chaves (cliente_id e produto_id).

# TODO 2: una pedidos e clientes para acrescentar nome, estado e segmento a
# cada pedido.

# TODO 3: acrescente também as informações dos produtos ao resultado anterior.

# TODO 4: escolha conscientemente entre inner, left, right ou outer join.
# Compare pelo menos duas opções e explique em um comentário a diferença na
# quantidade de linhas.

# TODO 5: use o recurso indicator do merge para encontrar pedidos sem cliente
# cadastrado e pedidos sem produto cadastrado.

# TODO 6: encontre clientes que nunca fizeram nenhum pedido.

# TODO 7: encontre produtos que nunca foram vendidos.

# TODO 8: crie valor_total multiplicando quantidade pelo preço do cadastro de
# produtos.

# TODO 9: calcule o faturamento por estado e por segmento de cliente.

# TODO 10: identifique o produto com maior faturamento e o produto com maior
# número de unidades vendidas.

# TODO 11: gere uma tabela final com uma linha por cliente contendo: nome,
# número de pedidos, total de unidades e valor total gasto. Inclua clientes
# sem pedidos com valores iguais a zero.

