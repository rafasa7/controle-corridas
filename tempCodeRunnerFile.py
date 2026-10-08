from datetime import datetime
corridas = []
def cadastrar_corrida():

    valor = float(input("Digite o valor da corrida: R$ "))
    distancia = float(input("Digite a distância percorrida (km): "))

    data = datetime.now().strftime("%d/%m/%Y")

    corrida = {
        "valor": valor,
        "distancia": distancia,
        "data": data
    }

    corridas.append(corrida)

    print(f"\nCorrida cadastrada! Valor: R$ {valor} e distância: {distancia}km")

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

    total = sum(corrida["valor"] for corrida in corridas)

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
    
    else:
        total = sum(corrida["valor"] for corrida in corridas)
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