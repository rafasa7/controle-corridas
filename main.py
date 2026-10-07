from datetime import datetime
corridas = []

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
        valor = float(input("Digite o valor da corrida: R$ "))
        distancia = float(input("Digite a distância percorrida (km): "))
        data = datetime.now().strftime("%d/%m/%Y")
        corrida = {
            "valor": valor,
            "distancia": distancia,
            "data": data
        }

        corridas.append(corrida)

        print(f"\nCorrida cadastrada! Valor: R$ {valor} e distáncia: {distancia}km")

    elif opcao == "2":
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

    elif opcao == "3":
        total = sum(corrida["valor"] for corrida in corridas)

        print(f"\nTotal ganho: R$ {total:.2f}")

    elif opcao == "4":
        if len(corridas) == 0:
            print("\nNenhuma corrida cadastrada.")
        else:
            total_ganho = sum(corrida["valor"] for corrida in corridas)
            total_distancia = sum(corrida["distancia"] for corrida in corridas)

            ganho_por_km = total_ganho / total_distancia

            print(f"\nTotal ganho: R$ {total_ganho:.2f}")
            print(f"Total percorrido: {total_distancia:.2f} km")
            print(f"Ganho por km: R$ {ganho_por_km:.2f}")

    elif opcao == "5":
        if len(corridas) == 0:
            print("Nenhuma corrida cadastrada.")

        else:
            total = sum(corrida["valor"] for corrida in corridas)
            print(f"\nA média é {total / len(corridas)}")

    elif opcao == "6":
        print("\nEncerrando o sistema. Até mais!")
        break


    else:
        print("\nOpção inválida. Tente novamente.")