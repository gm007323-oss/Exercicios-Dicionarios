menores = []
maiores = []

for i in range(10):
    print(f"\nCadastro da pessoa {i + 1}")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    pessoa = {
        "nome": nome,
        "idade": idade
    }

    if idade < 18:
        menores.append(pessoa)
    else:
        maiores.append(pessoa)

# Resultados
print("\n===== PESSOAS COM MENOS DE 18 ANOS =====")

for pessoa in menores:
    print(f"Nome: {pessoa['nome']} | Idade: {pessoa['idade']} anos")

print("\n===== PESSOAS COM 18 ANOS OU MAIS =====")

for pessoa in maiores:
    print(f"Nome: {pessoa['nome']} | Idade: {pessoa['idade']} anos")