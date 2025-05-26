# construtivo.py (Lógica C++ - Versão Limpa)
import math
from grafo import Grafo

def gerar_solucao_viavel(dados):
    """
    Gera uma solução viável usando a heurística de inserção mais barata.
    """
    capacidade = dados["capacidade"]
    deposito = dados["deposito"]
    reqs = dados["requisitos"]

    g = Grafo(dados)
    caminhos, custos = g.todos_menores_caminhos()

    servicos = []
    id_global = 1
    for s_type, s_list in [('N', reqs["nos"]), ('E', reqs["arestas"]), ('A', reqs["arcos"])]:
        for s_orig in s_list:
            s = s_orig.copy()
            s['tipo'] = s_type
            s['global_id'] = id_global
            s['atendido'] = False
            servicos.append(s)
            id_global += 1

    total_servicos = len(servicos)
    servicos_atendidos_cont = 0
    rotas_finais = []

    while servicos_atendidos_cont < total_servicos:
        servicos_atendidos_antes = servicos_atendidos_cont

        carga_atual = 0
        custo_rota = 0.0
        seq_serv_rota = []
        pos_atual = deposito

        while True:
            melhor_indice = -1
            menor_custo_insercao = math.inf
            p1_escolhido, p2_escolhido = 0, 0
            prox_pos_escolhida = -1

            for i, s in enumerate(servicos):
                if s['atendido'] or (carga_atual + s['demanda'] > capacidade):
                    continue

                custo_candidato_atual = math.inf
                p1_temp, p2_temp, pos_final_temp = 0, 0, 0
                u, v = s['u'], s['v']
                s_custo = s['s_custo']
                t_custo = s['t_custo']

                if s['tipo'] == 'N':
                    custo_viagem = custos[pos_atual][u]
                    if custo_viagem != math.inf:
                        custo_candidato_atual = custo_viagem + s_custo
                        p1_temp, p2_temp, pos_final_temp = u, u, u

                elif s['tipo'] == 'E':
                    custo_vu = custos[pos_atual][u]
                    custo1 = (custo_vu + t_custo + s_custo) if custo_vu != math.inf else math.inf
                    custo_vv = custos[pos_atual][v]
                    custo2 = (custo_vv + t_custo + s_custo) if custo_vv != math.inf else math.inf

                    if custo1 <= custo2 and custo1 != math.inf:
                        custo_candidato_atual = custo1
                        p1_temp, p2_temp, pos_final_temp = u, v, v
                    elif custo2 < custo1 and custo2 != math.inf:
                        custo_candidato_atual = custo2
                        p1_temp, p2_temp, pos_final_temp = v, u, u

                elif s['tipo'] == 'A':
                    custo_viagem = custos[pos_atual][u]
                    if custo_viagem != math.inf:
                        custo_candidato_atual = custo_viagem + t_custo + s_custo
                        p1_temp, p2_temp, pos_final_temp = u, v, v

                if custo_candidato_atual < menor_custo_insercao:
                    menor_custo_insercao = custo_candidato_atual
                    melhor_indice = i
                    p1_escolhido = p1_temp
                    p2_escolhido = p2_temp
                    prox_pos_escolhida = pos_final_temp

            if melhor_indice != -1:
                servico_escolhido = servicos[melhor_indice]
                servico_escolhido['atendido'] = True
                servicos_atendidos_cont += 1
                carga_atual += servico_escolhido['demanda']
                custo_rota += menor_custo_insercao
                seq_serv_rota.append(f"(S {servico_escolhido['global_id']},{p1_escolhido},{p2_escolhido})")
                pos_atual = prox_pos_escolhida
            else:
                break

        if seq_serv_rota:
            custo_volta = custos[pos_atual][deposito]
            if custo_volta == math.inf:
                print(f"ERRO ({dados['nome']}): Sem caminho de volta de {pos_atual} para {deposito}!")
                custo_volta = 999999
            custo_rota += custo_volta
            rotas_finais.append({
                "servicos_str": seq_serv_rota,
                "demanda": carga_atual,
                "custo": custo_rota
            })

        if servicos_atendidos_cont == servicos_atendidos_antes and servicos_atendidos_cont < total_servicos:
            print(f"AVISO CRÍTICO ({dados['nome']}): Loop estagnado. {total_servicos - servicos_atendidos_cont} serviços não atendidos. Parando.")
            break

    return rotas_finais