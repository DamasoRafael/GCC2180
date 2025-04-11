import math

def inicializar_matrizes(num_vertices, conexoes):
    # Inicializa as matrizes
    dist = [[math.inf] * (num_vertices + 1) for _ in range(num_vertices + 1)]
    pred = [[-1] * (num_vertices + 1) for _ in range(num_vertices + 1)]

    # Custo 0 do vértice para ele mesmo
    for i in range(1, num_vertices + 1):
        dist[i][i] = 0
        pred[i][i] = i

    # Adiciona as arestas/arcos ao grafo
    for u, v, custo, tipo in conexoes:
        if dist[u][v] > custo:
            dist[u][v] = custo
            pred[u][v] = u
        if tipo == 'E' and dist[v][u] > custo:  # Aresta é bidirecional
            dist[v][u] = custo
            pred[v][u] = v

    return dist, pred

def floyd_warshall(num_vertices, conexoes):
    dist, pred = inicializar_matrizes(num_vertices, conexoes)

    for k in range(1, num_vertices + 1):
        for i in range(1, num_vertices + 1):
            for j in range(1, num_vertices + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred
