# mainTeste.py (versão original sem checagem de conectividade)
import os
import time
from leitura import ler_instancia_completa
from construtivo import gerar_solucao_viavel

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    inst = "BHW1.dat"
    path = os.path.join(base, "Ins", inst)

    dados = ler_instancia_completa(path)

    t0 = time.perf_counter()
    rotas = gerar_solucao_viavel(dados)
    t1 = time.perf_counter()

    # calcula custo total diretamente com base na sequência dos nós
    custo_total = 0
    for nodes, _ in rotas:
        for i in range(len(nodes) - 1):
            u, v = nodes[i], nodes[i + 1]
            for a, b, custo, _ in dados["conexoes"]:
                if (a == u and b == v):
                    custo_total += custo
                    break

    clocks_heuristica = t1 - t0
    clocks_referencia = 0.0

    print(f"{int(custo_total)}")
    print(f"{len(rotas)}")
    print(f"{clocks_heuristica:.6f}")
    print(f"{clocks_referencia:.6f}")

    for nodes, seq in rotas:
        print("(D 0,1,1)", end=" ")
        for tipo, sid, u, v in seq:
            print(f"(S {sid},{u},{v})", end=" ")
        print("(D 0,1,1)")

if __name__ == "__main__":
    main()
