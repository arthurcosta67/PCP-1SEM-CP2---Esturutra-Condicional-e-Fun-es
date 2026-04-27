# dados
estado = int(input("Digite o estado de origem (1 a 5): "))
peso_toneladas = float(input("Digite o peso da carga em toneladas: "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))

# Converter de toneladas para quilos
peso_kg = peso_toneladas * 1000

# preço por kg
if 10 <= codigo_carga <= 20:
    preco_kg = 100.0
elif 21 <= codigo_carga <= 30:
    preco_kg = 250.0
else:
    preco_kg = 340.0

# Calcular preço da carga
preco_carga = peso_kg * preco_kg

# imposto
if estado == 1:
    imposto = 0.35
elif estado == 2:
    imposto = 0.25
elif estado == 3:
    imposto = 0.15
elif estado == 4:
    imposto = 0.05
else:
    imposto = 0.0

# Calcular valor do imposto
valor_imposto = preco_carga * imposto

# Calcular valor total
valor_total = preco_carga + valor_imposto

# Saída
print("Peso da carga em kg:", peso_kg)
print("Preço da carga:", preco_carga)
print("Valor do imposto:", valor_imposto)
print("Valor total transportado:", valor_total)