# rodar_todas.py (Versão Final para Processamento em Lote)
import os
import time
from leitura import ler_instancia_completa
# Certifique-se de que o construtivo.py limpo está salvo
from construtivo import gerar_solucao_viavel

def escrever_solucao_formato_pdf(nome_arquivo, rotas_info, custo_total, clocks_heuristica_secs):
    """
    Escreve a solução no formato especificado no PDF do trabalho.
    Converte o tempo para microsegundos (clocks).
    """
    # Converte segundos para microsegundos e arredonda para inteiro
    clocks_heuristica = int(round(clocks_heuristica_secs * 1_000_000))
    clocks_referencia = clocks_heuristica # Usamos o mesmo tempo, como no C++

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(f"{int(round(custo_total))}\n") # Custo total
        f.write(f"{len(rotas_info)}\n") # Total de rotas
        f.write(f"{clocks_heuristica}\n") # Clocks heurística (microsegundos)
        f.write(f"{clocks_referencia}\n") # Clocks referência (microsegundos)

        route_id = 1
        for rota in rotas_info:
            servicos_str = rota["servicos_str"] # Lista de "(S id,p1,p2)" strings
            custo_rota = rota["custo"]
            demanda_rota = rota["demanda"]

            total_visits = len(servicos_str) + 2

            # Linha de cabeçalho da rota
            f.write(f"0 1 {route_id} {demanda_rota} {int(round(custo_rota))} {total_visits} ")

            # Início no depósito (Literal, conforme exemplo)
            f.write("(D 0,1,1) ")

            # Sequência de serviços
            f.write(" ".join(servicos_str)) # Junta as strings de serviço

            # Fim no depósito (Literal, conforme exemplo)
            f.write(" (D 0,1,1)\n") # Adiciona o último D com espaço antes

            route_id += 1

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pasta_ins = os.path.join(base_dir, "Ins")
    pasta_saida = os.path.join(base_dir, "SolucoesFinais")

    if not os.path.exists(pasta_ins):
        print(f"ERRO: Pasta 'Ins' não encontrada em {pasta_ins}")
        return

    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)
        print(f"Pasta 'SolucoesFinais' criada em {pasta_saida}")

    # <<< ALTERAÇÃO AQUI: Lista TODOS os arquivos .dat >>>
    arquivos = sorted([f for f in os.listdir(pasta_ins) if f.endswith(".dat")])

    if not arquivos:
        print(f"ERRO: Nenhum arquivo .dat encontrado na pasta 'Ins'.")
        return

    total_arquivos = len(arquivos)
    print(f"Encontradas {total_arquivos} instâncias. Iniciando processamento...")

    start_time_total = time.time()

    for idx, fname in enumerate(arquivos):
        path = os.path.join(pasta_ins, fname)
        # Imprime o progresso
        print(f"[{idx + 1}/{total_arquivos}] Resolvendo: {fname}...")

        try:
            dados = ler_instancia_completa(path)

            t0 = time.time()
            rotas_info = gerar_solucao_viavel(dados)
            t1 = time.time()
            clocks_heuristica_secs = t1 - t0

            custo_total = sum(r["custo"] for r in rotas_info)

            # Define o nome do arquivo de saída (Ex: sol-BHW1.dat)
            saida = os.path.join(pasta_saida, f"sol-{fname}")
            
            escrever_solucao_formato_pdf(saida, rotas_info, custo_total, clocks_heuristica_secs)
            print(f"    -> Custo={int(round(custo_total))}, Rotas={len(rotas_info)}, Tempo={clocks_heuristica_secs:.4f}s. Salvo em {saida}")

        except Exception as e:
            print(f"    ERRO FATAL ao processar '{fname}': {e}")
            import traceback
            traceback.print_exc()
            continue # Pula para a próxima instância em caso de erro

    end_time_total = time.time()
    print(f"\n✅ Processamento concluído em {end_time_total - start_time_total:.2f} segundos.")
    print(f"Todas as {total_arquivos} soluções foram geradas em: {pasta_saida}")

if __name__ == "__main__":
    main()