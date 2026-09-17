"""Desafio final de análise de e-commerce (sem soluções)."""

from pathlib import Path

import pandas as pd


ARQUIVO = Path(__file__).resolve().parent.parent / "dados" / "ecommerce.csv"

# Contexto: cada linha representa um item de um pedido. Portanto, um mesmo
# pedido_id pode aparecer mais de uma vez.

# TODO 1: faça uma análise exploratória inicial e registre, em comentários,
# pelo menos três observações sobre a qualidade ou estrutura dos dados.

# TODO 2: converta as datas, trate valores ausentes e elimine duplicatas, caso
# existam. Não apague linhas sem antes justificar seu critério.

# TODO 3: crie valor_bruto e valor_liquido por item, considerando quantidade,
# preco_unitario e desconto_percentual.

# TODO 4: calcule os indicadores gerais: número de pedidos únicos, clientes
# únicos, itens vendidos, faturamento bruto, descontos concedidos e
# faturamento líquido.

# TODO 5: calcule o ticket médio por pedido. Cuidado para não calcular a média
# diretamente por linha de item.

# TODO 6: apresente o faturamento líquido por mês, categoria, região e canal.

# TODO 7: descubra os 5 clientes com maior gasto e mostre também quantos
# pedidos únicos cada um realizou.

# TODO 8: calcule o prazo de entrega em dias. Compare o prazo médio por região
# e por transportadora.

# TODO 9: considere atrasado todo pedido cuja entrega ocorreu após a
# data_prometida. Calcule a taxa de atraso geral e por transportadora.

# TODO 10: pedidos cancelados devem participar do faturamento? Produza duas
# versões do resultado e explique em comentário qual usaria em um relatório
# gerencial.

# TODO 11: crie uma tabela dinâmica mensal com as categorias nas colunas e o
# faturamento líquido nas células.

# TODO 12: exporte um resumo por pedido para dados/resumo_pedidos.csv. Cada
# pedido deve ocupar apenas uma linha.

# BÔNUS 1: crie pelo menos dois gráficos que comuniquem descobertas relevantes.

# BÔNUS 2: escreva, em comentários no fim do arquivo, três conclusões de
# negócio sustentadas pelos seus cálculos.

