corridas = []

print("=== CONTROLE DE CORRIDAS ===")

valor = float(input("Digite o valor da corrida: R$ "))
distancia = float(input("Digite a distância percorrida (km): "))

corrida = {
    "valor": valor,
    "distancia": distancia
}

corridas.append(corrida)

print("\nCorrida cadastrada com sucesso!")

print(f"Valor da corrida: R$ {valor:.2f}")
print(f"Distância percorrida: {distancia:.2f} km")
