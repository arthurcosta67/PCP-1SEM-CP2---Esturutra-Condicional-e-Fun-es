# Entrada das notas
cp1 = float(input("Digite a nota do CP1: "))
cp2 = float(input("Digite a nota do CP2: "))
cp3 = float(input("Digite a nota do CP3: "))
sp1 = float(input("Digite a nota da Sprint 1: "))
sp2 = float(input("Digite a nota da Sprint 2: "))
gs = float(input("Digite a nota da Global Solution: "))

# Encontrar a menor nota dos checkpoints
menor_cp = cp1

if cp2 < menor_cp:
    menor_cp = cp2

if cp3 < menor_cp:
    menor_cp = cp3

# Soma dos checkpoints sem a menor nota
soma_cp = cp1 + cp2 + cp3 - menor_cp

# Média do semestre (sem peso)
media_semestre = ((soma_cp + sp1 + sp2) / 4) * 0.4 + (gs * 0.6)

# Média com peso
media_com_peso = media_semestre * 0.4

# Saída
print(f"Média do semestre: {media_semestre:.1f}")
print(f"Média com peso: {media_com_peso:.1f}")