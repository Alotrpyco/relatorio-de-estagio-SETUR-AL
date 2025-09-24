# Calculadora de Horas de Estágio.
from datetime import datetime, timedelta


# Data que iniciou e data que terminou o estágio.
data_inicio = input("Digite a data de início (dd/mm/yyyy): ")
data_fim = input("Digite a data de fim (dd/mm/yyyy): ")

# Quantidade de horas por dia trabalhadas no estágio.
horas_por_dia = float(input("Digite quantas horas você trabalha por dia: "))

# Converter para datetime.
formato = "%d/%m/%Y"
inicio = datetime.strptime(data_inicio, formato)
fim = datetime.strptime(data_fim, formato)

# Garantir que a data final seja maior ou igual à inicial ( Validação da Data)
if fim < inicio:
    print("A data final deve ser maior ou igual à data inicial.")
else:
    # Contando dias úteis
    dias_uteis = 0
    data_atual = inicio
    while data_atual <= fim:
        if data_atual.weekday() < 5:  # 0=segunda, ..., 4=sexta
            dias_uteis += 1
        data_atual += timedelta(days=1)

    # Calculando horas totais
    horas_totais = dias_uteis * horas_por_dia

    print(f"\nPeríodo: {dias_uteis} dias úteis")
    print(f"Horas trabalhadas no total: {horas_totais} horas")
