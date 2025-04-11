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

## 🧑‍💻 Autor

Projeto desenvolvido por João Vitor Givisiez Lessa e Rafael Rabelo Pereira Damaso como parte da disciplina de Teoria dos Grafos — UFLA

---
