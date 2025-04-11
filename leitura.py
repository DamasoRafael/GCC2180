import re
import os

def ler_instancia_generica(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        # Lê todas as linhas e descarta as vazias
        linhas = [l.strip() for l in f if l.strip() != ""]

    # Inicializa o dicionário de dados
    dados = {
        "nome": os.path.basename(caminho),
        "capacidade": 0,
        "deposito": 0,
        "num_vertices": 0,
        "requisitos": {
            "nos": [],      # (id, demanda)
            "arestas": [],  # (u, v, custo, demanda)
            "arcos": []     # (u, v, custo, demanda)
        },
        "conexoes": []     # Poderá ser preenchido em outro módulo se necessário
    }

    # Loop para processar o cabeçalho e seções de requisitos
    i = 0
    while i < len(linhas):
        linha = linhas[i]

        # Cabeçalho geral:
        if linha.startswith("Name:"):
            # Exemplo: "Name:		BHW2"
            dados["nome"] = linha.split(":", 1)[1].strip()

        elif linha.startswith("Optimal value:"):
            # Se necessário, pode armazenar esse valor também
            pass

        elif linha.startswith("#Vehicles:"):
            # Pode ser ignorado se não for necessário para a montagem do grafo
            pass

        elif linha.startswith("Capacity:"):
            dados["capacidade"] = int(re.findall(r'\d+', linha)[0])

        elif linha.startswith("Depot Node:"):
            dados["deposito"] = int(re.findall(r'\d+', linha)[0])

        elif linha.startswith("#Nodes:"):
            dados["num_vertices"] = int(re.findall(r'\d+', linha)[0])

        # Seções de requisitos. Note que os rótulos podem ser:
        # "#Required N:"  — mas os dados reais vêm na tabela "ReN."
        # Assim, a leitura dos valores requeridos será feita pelos blocos abaixo.

        # Bloco de Nós requeridos (ReN.)
        elif linha.upper().startswith("REN."):
            i += 1
            while i < len(linhas):
                prox = linhas[i]
                # Se a linha começar com "ReE.", "ReA.", "EDGE", "ARC" ou se for cabeçalho (contendo "DEMAND" etc.), encerra o bloco.
                if prox.upper().startswith(("REE.", "REA.", "EDGE", "ARC")) or re.search(r"DEMAND", prox.upper()):
                    # Se encontrar cabeçalho ("DEMAND" etc.) e depois dados, ignore o cabeçalho e continue
                    # Assim, se a próxima linha não iniciar com "N" ou não tiver número, pulamos.
                    if prox.upper().startswith("REN."):  # redundante
                        i += 1
                        continue
                    else:
                        break
                try:
                    partes = prox.split()
                    # Exemplo: "N11	1	1"  → partes[0]="N11", partes[1]="1", partes[2]="1"
                    if partes[0].upper().startswith("N"):
                        no = int(partes[0][1:])
                    else:
                        no = int(partes[0])
                    demanda = int(partes[1])
                    # Podemos ignorar o custo de serviço (parts[2]) ou armazená-lo se necessário
                    dados["requisitos"]["nos"].append((no, demanda))
                except (ValueError, IndexError):
                    # Caso a linha não possua o formato esperado, ignora
                    pass
                i += 1
            continue

        # Bloco de Arestas requeridas (ReE.)
        elif linha.upper().startswith("REE."):
            # Avança para ignorar o cabeçalho da tabela se existir (ex.: "FROM N.  TO N.  T. COST  DEMAND  S. COST")
            i += 1
            while i < len(linhas):
                prox = linhas[i]
                # Se a linha for um cabeçalho identificável (contendo "FROM" e "TO") ou iniciar outro bloco, sai
                if prox.upper().startswith(("REA.", "REN.", "EDGE", "ARC")) or ("FROM" in prox.upper() and "TO" in prox.upper()):
                    i += 1
                    continue
                # Se a linha não tiver dígitos, encerra o bloco
                if not re.search(r"\d", prox):
                    break
                try:
                    partes = prox.split()
                    # Espera-se pelo menos 6 colunas: [id, from, to, cost, demand, ...]
                    if len(partes) >= 6:
                        u = int(partes[1])
                        v = int(partes[2])
                        custo = int(partes[3])
                        demanda = int(partes[4])
                        dados["requisitos"]["arestas"].append((u, v, custo, demanda))
                    # Em alguns casos pode haver apenas 4 colunas
                    elif len(partes) == 4:
                        u, v, custo, demanda = map(int, partes)
                        dados["requisitos"]["arestas"].append((u, v, custo, demanda))
                except (ValueError, IndexError):
                    pass
                i += 1
            continue

        # Bloco de Arcos requeridos (ReA.)
        elif linha.upper().startswith("REA."):
            i += 1
            while i < len(linhas):
                prox = linhas[i]
                if prox.upper().startswith(("REE.", "REN.", "EDGE", "ARC")) or ("FROM" in prox.upper() and "TO" in prox.upper()):
                    i += 1
                    continue
                if not re.search(r"\d", prox):
                    break
                try:
                    partes = prox.split()
                    if len(partes) >= 6:
                        u = int(partes[1])
                        v = int(partes[2])
                        custo = int(partes[3])
                        demanda = int(partes[4])
                        dados["requisitos"]["arcos"].append((u, v, custo, demanda))
                    elif len(partes) == 4:
                        u, v, custo, demanda = map(int, partes)
                        dados["requisitos"]["arcos"].append((u, v, custo, demanda))
                except (ValueError, IndexError):
                    pass
                i += 1
            continue

        # Seção de conexões gerais (EDGE ou ARC) – opcional, caso exista.
        # Se necessário, você pode implementar a leitura dessa seção para construir "conexoes" completas.
        elif linha.upper().startswith("EDGE") or linha.upper().startswith("ARC"):
            i += 1
            while i < len(linhas):
                prox = linhas[i]
                if not prox or prox.upper().startswith(("REN.", "REE.", "REA.")):
                    break
                try:
                    partes = prox.split()
                    # Exemplo: "FROM N.	TO N.	T. COST" pode ser cabeçalho, então tente identificar linhas com números.
                    if len(partes) >= 4 and re.search(r"\d", partes[1]):
                        u = int(partes[1])
                        v = int(partes[2])
                        custo = int(partes[3])
                        # Aqui, por padrão, consideramos essas conexões como arestas bidirecionais
                        dados["conexoes"].append((u, v, custo, 'E'))
                        dados["conexoes"].append((v, u, custo, 'E'))
                except (ValueError, IndexError):
                    pass
                i += 1
            continue

        i += 1

    return dados

# Para os demais tipos, se o formato for similar, utilizamos a mesma função.
def ler_bhw(caminho): return ler_instancia_generica(caminho)
def ler_cbmix(caminho): return ler_instancia_generica(caminho)
def ler_dinearp(caminho): return ler_instancia_generica(caminho)
def ler_mggdb(caminho): return ler_instancia_generica(caminho)
def ler_mgval(caminho): return ler_instancia_generica(caminho)

def ler_instancia_por_tipo(caminho):
    nome = os.path.basename(caminho).lower()
    if nome.startswith("bhw"):
        return ler_bhw(caminho)
    elif nome.startswith("cbmix"):
        return ler_cbmix(caminho)
    elif nome.startswith("di-nearp") or nome.startswith("dinearp"):
        return ler_dinearp(caminho)
    elif nome.startswith("mggdb"):
        return ler_mggdb(caminho)
    elif nome.startswith("mgval"):
        return ler_mgval(caminho)
    else:
        raise ValueError(f"Tipo de instância desconhecido para o arquivo: {nome}")
