# Função para calcular horas extras
def calcular_horas_extras(salario_base, horas):
    return salario_base * 0.015 * horas

# Função para calcular descontos por faltas
def calcular_descontos_faltas(salario_base, faltas):
    return salario_base * 0.02 * faltas

# Função para calcular bônus
def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == 's':
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        elif cargo == 4:
            return 100
    return 0

# Entrada de dados
nome = input("Digite o nome do funcionário: ")
cargo = int(input("Digite o cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
salario_base = float(input("Digite o salário base: "))
horas_extras = float(input("Digite o total de horas extras: "))
faltas = int(input("Digite o total de faltas: "))
recebeu_bonus = input("Recebeu bônus? (s/n): ").lower()

# Cálculos
valor_horas_extras = calcular_horas_extras(salario_base, horas_extras)
valor_descontos = calcular_descontos_faltas(salario_base, faltas)
valor_bonus = calcular_bonus(cargo, recebeu_bonus)

total_acrescimos = valor_horas_extras + valor_bonus
salario_bruto = salario_base + total_acrescimos
salario_final = salario_bruto - valor_descontos

# Saída
print(f"\nFuncionário: {nome}")
print(f"Salário bruto: {salario_bruto:.2f}")
print(f"Total de acréscimos: {total_acrescimos:.2f}")
print(f"Total de descontos: {valor_descontos:.2f}")
print(f"Salário final: {salario_final:.2f}")