"""Exercícios de séries temporais com pandas (sem soluções)."""

from pathlib import Path

import pandas as pd


ARQUIVO = Path(__file__).resolve().parent.parent / "dados" / "cotacoes.csv"

# Os valores deste dataset são fictícios e servem somente para estudo.

# TODO 1: leia os dados, converta data para datetime e use-a como índice.

# TODO 2: ordene cronologicamente e verifique se existem datas repetidas ou
# valores ausentes.

# TODO 3: calcule a variação percentual diária de cada ativo.

# TODO 4: descubra o melhor e o pior dia de cada ativo com base na variação
# percentual diária.

# TODO 5: calcule uma média móvel de 5 observações para cada ativo.

# TODO 6: transforme os dados do formato longo para o formato largo, deixando
# uma coluna de preço para cada ativo.

# TODO 7: calcule a correlação entre as variações diárias dos ativos.

# TODO 8: reamostre os preços por semana e obtenha o último preço de cada
# semana.

# TODO 9: calcule o retorno acumulado de cada ativo no período, considerando
# o primeiro e o último preço disponível.

# TODO 10: crie um gráfico de linhas com a evolução dos preços e outro com as
# médias móveis. Adicione título, legenda e rótulos dos eixos.

