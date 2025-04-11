class Grafo:
    def __init__(self, dados):
        self.nome = dados.get('nome')
        self.capacidade = dados.get('capacidade', 0)
        self.deposito = dados.get('deposito', 0)
        self.num_vertices = dados.get('num_vertices', 0)

        # Requisitos
        self.nos_requeridos = dados['requisitos'].get('nos', [])          # (id, demanda)
        self.arestas_requeridas = dados['requisitos'].get('arestas', [])  # (u, v, custo, demanda)
        self.arcos_requeridos = dados['requisitos'].get('arcos', [])      # (u, v, custo, demanda)

        # Conexões (para usar com floyd ou estatísticas)
        self.conexoes = []

        # Arestas são bidirecionais
        for u, v, custo, *_ in self.arestas_requeridas:
            self.conexoes.append((u, v, custo, 'E'))
            self.conexoes.append((v, u, custo, 'E'))

        # Arcos são direcionais
        for u, v, custo, *_ in self.arcos_requeridos:
            self.conexoes.append((u, v, custo, 'A'))

def construir_grafo(dados):
    return Grafo(dados)
