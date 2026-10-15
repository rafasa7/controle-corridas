import json
from datetime import datetime
corridas = []
def salvar_corridas():
    with open("corridas.json", "w", encoding="utf-8") as arquivo:
        json.dump(corridas, arquivo, ensure_ascii=False, indent=4)

def carregar_corridas():
    global corridas

    try:
        with open("corridas.json", "r", encoding="utf-8") as arquivo:
            corridas = json.load(arquivo)

    except FileNotFoundError:
        corridas = []

def cadastrar_corrida():

    try:
        valor = float(input("Digite o valor da corrida: R$ "))
    except ValueError:
        print("Erro: digite um valor numérico válido.")
        return

    if valor < 0:
        print("TESTE: entrei na validação")
        return

    try:
        distancia = float(input("Digite a distância percorrida (km): "))
    except ValueError:
        print("Erro: digite uma distância numérica válida.")
        return

    if distancia <= 0:
        print("Erro: a distância precisa ser maior que zero.")
        return

    data = datetime.now().strftime("%d/%m/%Y")

    corrida = {
        "valor": valor,
        "distancia": distancia,
        "data": data
    }

    corridas.append(corrida)
    salvar_corridas()

    print(f"\nCorrida cadastrada! Valor: R$ {valor} e distância: {distancia}km")

carregar_corridas()

def listar_corridas():
    print("\n=== CORRIDAS CADASTRADAS ===")
    
    if len(corridas) == 0:
        print("Nenhuma corrida cadastrada.")
    else:
        for i, corrida in enumerate(corridas, start=1):
            print(
                        f"{i} - R$ {corrida['valor']:.2f} | "
                        f"{corrida['distancia']:.2f} km | "
                        f"{corrida['data']}"
                    )

def calcular_total():
    total = 0

    for corrida in corridas:
        total += corrida["valor"]

    return total

def calcular_ganho_por_km():

    if len(corridas) == 0:
        return 0

    total_ganho = calcular_total()

    total_distancia =  sum(corrida["distancia"] for corrida in corridas)

    ganho_por_km = total_ganho / total_distancia

    return ganho_por_km

def calcular_media():
    if len(corridas) == 0:
        return 0

    total = 0

    for corrida in corridas:
        total += corrida["valor"]

    return total / len(corridas)
    


while True:
    print("\n=== CONTROLE DE CORRIDAS ===")
    print("1 - Cadastrar corrida")
    print("2 - Ver corridas cadastradas")
    print("3 - Ver total ganho")
    print("4 - Ver ganho por km")
    print("5 - Ver média por corrida")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_corrida()

    elif opcao == "2":
        listar_corridas()

    elif opcao == "3":
        total = calcular_total()
        print(f"\nTotal ganho: R$ {total:.2f}")

    elif opcao == "4":
        ganho_por_km = calcular_ganho_por_km()

        if ganho_por_km == 0:
            print("\nNenhuma corrida cadastrada.")
        else:
            print(f"\nGanho por km: R$ {ganho_por_km:.2f}")

    elif opcao == "5":
        media = calcular_media()

        if media == 0:
            print("\nNenhuma corrida cadastrada.")
        else:
            print(f"\nMédia por corrida: R$ {media:.2f}")

    elif opcao == "6":
        print("\nEncerrando o sistema. Até mais!")
        break


    else:
        print("\nOpção inválida. Tente novamente.")

salvar_corridas()
print("Corridas salvas com sucesso!")