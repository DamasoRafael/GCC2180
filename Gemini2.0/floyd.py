# floyd.py (Versão Limpa)
import math

def inicializar_matrizes(num_vertices, conexoes):
    """
    Inicializa as matrizes de distância e predecessores.
    """
    n = num_vertices
    dist = [[math.inf] * (n + 1) for _ in range(n + 1)]
    pred = [[-1]        * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dist[i][i] = 0
        pred[i][i] = i

    for u, v, custo, tipo in conexoes:
        if 1 <= u <= n and 1 <= v <= n:
            if dist[u][v] > custo:
                dist[u][v] = custo
                pred[u][v] = u
            if tipo in ("E", "NE") and dist[v][u] > custo:
                dist[v][u] = custo
                pred[v][u] = v
    return dist, pred

def floyd_warshall(num_vertices, conexoes):
    """
    Executa o algoritmo de Floyd-Warshall (loops 1-Based).
    """
    dist, pred = inicializar_matrizes(num_vertices, conexoes)
    n = num_vertices

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] != math.inf and dist[k][j] != math.inf:
                    via_k = dist[i][k] + dist[k][j]
                    if via_k < dist[i][j]:
                        dist[i][j] = via_k
                        pred[i][j] = pred[k][j]

    return dist, pred