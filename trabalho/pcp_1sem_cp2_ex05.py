# Verifica aprovação
def pode_aprovar(idade, renda, valor):
    if idade > 18 and valor <= renda * 20:
        return True
    return False

# Define taxa de juros
def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10

# Fórmula correta da Tabela
def calcular_parcela(valor, taxa, parcelas):
    return valor * (taxa * (1 + taxa) ** parcelas) / ((1 + taxa) ** parcelas - 1)

# Total pago
def calcular_total(parcela, parcelas):
    return parcela * parcelas

# Juros pagos
def calcular_juros(total, valor):
    return total - valor


# Entrada
nome = input("Nome do cliente: ")
idade = int(input("Idade: "))
renda = float(input("Renda mensal: "))
valor = float(input("Valor do empréstimo: "))
parcelas = int(input("Número de parcelas (3 a 24): "))

# Processamento
if pode_aprovar(idade, renda, valor):
    taxa = definir_taxa(parcelas)
    parcela = calcular_parcela(valor, taxa, parcelas)
    total = calcular_total(parcela, parcelas)
    juros = calcular_juros(total, valor)

    print("\nEMPRÉSTIMO APROVADO")
    print("Cliente:", nome)
    print(f"Valor financiado: {valor:.2f}")
    print(f"Taxa de juros: {taxa*100:.0f}% ao mês")
    print(f"Valor da parcela: {parcela:.2f}")
    print(f"Valor total pago: {total:.2f}")
    print(f"Total de juros pagos: {juros:.2f}")
else:
    print("\nEMPRÉSTIMO NEGADO")