# grafo.py (Versão Limpa)
import math
from floyd import floyd_warshall

class Grafo:
    def __init__(self, dados):
        n_header = dados["num_vertices"]
        self.n = n_header
        if dados["conexoes"]:
            max_conn = max(max(u, v) for u, v, _, _ in dados["conexoes"])
            if max_conn > self.n:
                print(f"AVISO: Nó {max_conn} encontrado ({dados['nome']}), mas #NODES é {n_header}. Usando {max_conn}.")
                self.n = max_conn
        self.conexoes = dados["conexoes"]

    def todos_menores_caminhos(self):
        dist, pred = floyd_warshall(self.n, self.conexoes)
        caminhos = [[[] for _ in range(self.n + 1)] for __ in range(self.n + 1)]

        for i in range(self.n + 1):
            for j in range(self.n + 1):
                if dist[i][j] == math.inf or pred[i][j] == -1:
                    caminhos[i][j] = []
                else:
                    path = []
                    k = j
                    while k != i:
                        if k == -1:
                            path = []
                            break
                        path.append(k)
                        k = pred[i][k]
                    if k != -1:
                        path.append(i)
                        caminhos[i][j] = path[::-1]

        return caminhos, dist