# Prática de pandas

Esta pasta contém exercícios progressivos de análise de dados com pandas.
Os enunciados estão escritos como comentários nos arquivos da pasta
`exercicios/`. Os datasets correspondentes ficam em `dados/`.

## Ordem sugerida

1. `01_fundamentos.py` — leitura, inspeção, seleção e filtros
2. `02_limpeza.py` — valores ausentes, duplicatas e padronização
3. `03_agrupamentos.py` — `groupby`, agregações e tabelas dinâmicas
4. `04_juncoes.py` — combinação de tabelas com `merge`
5. `05_series_temporais.py` — datas, variações e médias móveis
6. `06_desafio_ecommerce.py` — análise completa juntando os assuntos anteriores

## Como executar

Instale as dependências uma vez:

```bash
python -m pip install -r requirements.txt
```

Na raiz deste projeto, execute por exemplo:

```bash
python exercicios/01_fundamentos.py
```

Os arquivos contêm apenas a preparação mínima e os enunciados. Escreva suas
respostas logo abaixo de cada comentário `TODO`. Quando um exercício pedir uma
alteração, prefira criar uma nova coluna ou um novo DataFrame para conseguir
comparar o antes e o depois.
