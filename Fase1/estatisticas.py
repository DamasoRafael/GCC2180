def contar_vertices(grafo):
    return grafo.num_vertices

def contar_arestas(grafo):
    total = len(grafo.arestas_requeridas)
    if hasattr(grafo, 'arestas_nao_requeridas'):
        total += len(grafo.arestas_nao_requeridas)
    return total

def contar_arcos(grafo):
    total = len(grafo.arcos_requeridos)
    if hasattr(grafo, 'arcos_nao_requeridos'):
        total += len(grafo.arcos_nao_requeridos)
    return total

def contar_vertices_requeridos(grafo):
    return len(grafo.nos_requeridos)

def contar_arestas_requeridas(grafo):
    return len(grafo.arestas_requeridas)

def contar_arcos_requeridos(grafo):
    return len(grafo.arcos_requeridos)

def calcular_densidade(grafo):
    V = grafo.num_vertices
    A = contar_arestas(grafo) + contar_arcos(grafo)
    return A / (V * (V - 1)) if V > 1 else 0

def componentes_conectados(grafo):
    visitado = set()
    componentes = 0
    adj = {i: [] for i in range(1, grafo.num_vertices + 1)}

    for u, v, _, tipo in grafo.conexoes:
        adj[u].append(v)
        if tipo == 'E':
            adj[v].append(u)

    def dfs(v):
        visitado.add(v)
        for vizinho in adj[v]:
            if vizinho not in visitado:
                dfs(vizinho)

    for v in range(1, grafo.num_vertices + 1):
        if v not in visitado:
            componentes += 1
            dfs(v)

    return componentes

def calcular_graus(grafo):
    graus = {i: 0 for i in range(1, grafo.num_vertices + 1)}

    for u, v, _, tipo in grafo.conexoes:
        graus[u] += 1
        if tipo == 'E':
            graus[v] += 1

    valores = graus.values()
    return min(valores), max(valores)

def grau_minimo(grafo):
    minimo, _ = calcular_graus(grafo)
    return minimo

def grau_maximo(grafo):
    _, maximo = calcular_graus(grafo)
    return maximo

def intermediacao(grafo, matriz_distancias):
    V = grafo.num_vertices
    intermediacoes = {i: 0 for i in range(1, V + 1)}

    for s in range(1, V + 1):
        for t in range(1, V + 1):
            if s != t and matriz_distancias[s][t] != float('inf'):
                for v in range(1, V + 1):
                    if v != s and v != t:
                        if matriz_distancias[s][v] + matriz_distancias[v][t] == matriz_distancias[s][t]:
                            intermediacoes[v] += 1
                            break  # já encontrou um caminho passando por v

    return intermediacoes

def caminho_medio(matriz_distancias):
    total = 0
    cont = 0
    V = len(matriz_distancias) - 1
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if i != j and matriz_distancias[i][j] != float('inf'):
                total += matriz_distancias[i][j]
                cont += 1
    return total / cont if cont > 0 else 0

def diametro(matriz_distancias):
    diam = 0
    V = len(matriz_distancias) - 1
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if matriz_distancias[i][j] != float('inf'):
                diam = max(diam, matriz_distancias[i][j])
    return diam
