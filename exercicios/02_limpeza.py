"""Exercícios de limpeza e preparação de dados (sem soluções)."""

from pathlib import Path

import pandas as pd


ARQUIVO = Path(__file__).resolve().parent.parent / "dados" / "clientes_sujos.csv"

# TODO 1: carregue o dataset e faça uma inspeção inicial (linhas, colunas,
# tipos e quantidade de valores ausentes por coluna).

# TODO 2: identifique as linhas completamente duplicadas e remova as cópias.

# TODO 3: verifique se existem IDs repetidos com informações diferentes.
# Mantenha apenas um registro por cliente e anote em um comentário o critério
# que você escolheu para decidir qual registro preservar.

# TODO 4: remova espaços extras no começo e no fim dos nomes.

# TODO 5: padronize os nomes das cidades (há diferenças de maiúsculas,
# minúsculas, acentos e espaços).

# TODO 6: converta a coluna data_cadastro para datetime. Alguns registros
# possuem formatos diferentes e um deles é inválido.

# TODO 7: converta renda_mensal para número. Trate os valores que não puderem
# ser convertidos e escolha uma estratégia para os valores ausentes.

# TODO 8: padronize os e-mails em letras minúsculas e identifique endereços
# que não contêm o caractere @.

# TODO 9: padronize a coluna ativo para conter somente os valores booleanos
# True e False.

# TODO 10: crie um relatório simples com a quantidade de problemas encontrados
# em cada coluna antes da limpeza.

# TODO 11: salve o DataFrame limpo como dados/clientes_limpos.csv sem gravar
# o índice do pandas.

