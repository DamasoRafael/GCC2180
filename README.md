# GCC218 - Projeto de Grafos

Este é um projeto desenvolvido na disciplina **GCC218 - Teoria dos Grafos** (UEM) com o objetivo de implementar uma solução completa para leitura, modelagem e análise de grafos a partir de instâncias fornecidas em arquivos `.dat`.

---

## 📌 Objetivo

O projeto realiza:

- Leitura de instâncias de grafos em arquivos `.dat`
- Construção da estrutura do grafo (arestas, arcos, vértices, pesos, etc.)
- Cálculo de diversas métricas e estatísticas do grafo
- Geração de uma **tabela formatada com os resultados** no Jupyter Notebook

---

Fase 1:

## 🧱 Estrutura do Projeto

```
gcc218/
│
├── estatisticas.py          # Funções para calcular métricas dos grafos
├── floyd.py                 # Algoritmo de Floyd-Warshall para distâncias mínimas
├── grafo.py                 # Estrutura e construção de grafos
├── leitura.py               # Leitura e parsing de arquivos .dat
├── main.py                  # Execução do pipeline completo
├── Ins/                     # Diretório com instâncias (.dat)
│   ├── BHW2.dat
│   └── ...
└── notebook.ipynb           # Jupyter notebook com análise final (opcional)
```

---

## 📦 Requisitos

- Python 3.9 ou superior
- Jupyter Notebook
- `pandas` (para exibição tabular)

Instale as dependências com:

```bash
pip install pandas notebook
```

---

## ▶️ Como executar

1. Baixe a pasta do GitHub

2. Certifique-se de que a pasta `Ins/` contém as instâncias `.dat`.

3. No terminal, rode o script (opcional):

```bash
python main.py
```

4. **Ou execute no Jupyter Notebook** para gerar uma tabela visual:

```bash
jupyter notebook
```

E use o código do arquivo teste.ipynb no notebook

`

## 📊 Métricas Calculadas

O projeto calcula automaticamente:

- Quantidade de vértices
- Quantidade de arestas
- Quantidade de arcos
- Quantidade de elementos requeridos
- Densidade
- Componentes conectados
- Graus
- Intermediação
- Excentricidade
- Caminho médio
- Diâmetro

---

## 🧠 Algoritmos Implementados

- Floyd-Warshall para cálculo de distâncias mínimas
- Cálculo de métricas topológicas clássicas de grafos
- Leitura genérica de instâncias com parsing estruturado

---

Fase 2: Heurística Construtiva para Roteamento
A segunda fase do projeto consistiu em desenvolver um algoritmo construtivo para gerar uma solução inicial viável para o Problema de Roteamento de Arcos Capacitado (CARP).

Algoritmo Implementado: Heurística de Inserção Mais Barata

A abordagem escolhida foi uma heurística gulosa que constrói as rotas iterativamente, sempre escolhendo o próximo serviço que pode ser atendido com o menor custo adicional.

Lógica do Algoritmo:

Inicialização: As distâncias de caminho mínimo entre todos os nós são pré-calculadas usando o Floyd-Warshall da Fase 1.
Construção de Rota: Uma nova rota é iniciada no depósito, com carga e custo zerados.
Seleção do Serviço: Em cada passo, o algoritmo avalia todos os serviços ainda não atendidos e calcula o "custo de inserção" para cada um, que consiste em:
Custo de Deslocamento: Custo do caminho mínimo da posição atual do veículo até o início do serviço.
Custo de Execução: Soma do custo de travessia e do custo de serviço da tarefa.
Adição à Rota: O serviço com o menor custo de inserção que não viola a capacidade máxima do veículo é adicionado à rota. A posição atual, a carga e o custo da rota são atualizados.
Finalização: O processo se repete até que nenhum serviço possa mais ser adicionado à rota atual. A rota é então finalizada com o deslocamento de volta ao depósito. Se ainda restarem serviços, uma nova rota é iniciada.
Geração de Solução: O resultado final é um conjunto de arquivos sol-*.dat, um para cada instância, descrevendo as rotas, custos e demandas, conforme o formato especificado.
🧱 Estrutura do Projeto
gcc218/
│
├── construtivo.py           # Heurística construtiva da Fase 2
├── floyd.py                 # Algoritmo de Floyd-Warshall
├── grafo.py                 # Estrutura e construção de grafos
├── leitura.py               # Leitura e parsing de arquivos .dat
├── rodar_todas.py           # Script principal para executar todas as instâncias
├── README.md                # Este arquivo
│
├── Ins/                     # Diretório com as instâncias (.dat)
│   ├── BHW1.dat
│   └── ...
│
└── SolucoesFinais/          # Diretório para salvar os arquivos de solução gerados
    ├── sol-BHW1.dat
    └── ...
▶️ Como executar
Clone ou baixe o repositório do GitHub. 
Certifique-se de que a pasta Ins/ contém as instâncias .dat. 
No terminal, execute o script principal para gerar as soluções para todas as instâncias:
Bash

python rodar_todas.py
As soluções serão salvas na pasta SolucoesFinais/.

## 🧑‍💻 Autor

Projeto desenvolvido por João Vitor Givisiez Lessa e Rafael Rabelo Pereira Damaso como parte da disciplina de Teoria dos Grafos — UFLA

---
