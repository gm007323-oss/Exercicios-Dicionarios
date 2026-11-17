import csv

moedas = []

with open("moedas.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        moedas.append(linha)

valor = float(input("Digite o valor em R$: "))
destino = input("Digite a moeda de destino: ").upper()

# conversão
encontrou = False

for moeda in moedas:
    if moeda["moeda"].upper() == destino:

        cotacao = float(moeda["cotacao"])
        convertido = valor / cotacao

        print("\n===== RESULTADO DA CONVERSÃO =====")
        print(f"Moeda: {moeda['nome']}")
        print(f"Valor convertido: {convertido:.2f} {destino}")

        encontrou = True
        break

if not encontrou:
    print("Moeda não encontrada!")