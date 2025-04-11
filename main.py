from leitura import ler_instancia_por_tipo
from grafo import construir_grafo
from floyd import floyd_warshall
import estatisticas 

def main():
    # Caminho do arquivo .dat da instância (altere aqui para testar outras)
    caminho_instancia = "Ins/BHW3.dat"

    # Leitura da instância
    dados = ler_instancia_por_tipo(caminho_instancia)
    grafo = construir_grafo(dados)

    # Matriz de distâncias
    dist, _ = floyd_warshall(grafo.num_vertices, grafo.conexoes)

    # Estatísticas
    print(f"\n>>> Estatísticas da instância: {grafo.nome}")
    print(f"Vértices: {estatisticas.contar_vertices(grafo)}")
    print(f"Arestas: {estatisticas.contar_arestas(grafo)}")
    print(f"Arcos: {estatisticas.contar_arcos(grafo)}")
    print(f"Vértices requeridos: {estatisticas.contar_vertices_requeridos(grafo)}")
    print(f"Arestas requeridas: {estatisticas.contar_arestas_requeridas(grafo)}")
    print(f"Arcos requeridos: {estatisticas.contar_arcos_requeridos(grafo)}")
    print(f"Densidade: {round(estatisticas.calcular_densidade(grafo), 4)}")
    print(f"Componentes conectados: {estatisticas.componentes_conectados(grafo)}")
    print(f"Grau mínimo: {estatisticas.grau_minimo(grafo)}")
    print(f"Grau máximo: {estatisticas.grau_maximo(grafo)}")
    print(f"Caminho médio: {round(estatisticas.caminho_medio(dist), 4)}")
    print(f"Diâmetro: {estatisticas.diametro(dist)}")

    # Intermediação
    print("\n>>> Intermediação por vértice:")
    intermediacao = estatisticas.intermediacao(grafo, dist)
    for vertice in sorted(intermediacao.keys()):
        print(f"Vértice {vertice}: {intermediacao[vertice]}")

if __name__ == "__main__":
    main()
