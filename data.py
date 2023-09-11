#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

def data_valida(data):
    try:
        # Divide a data em dia, mês e ano
        dia, mes, ano = map(int, data.split('/'))

        # Verifica se o ano está no formato correto (4 dígitos)
        if len(str(ano)) != 4:
            return False

        # Verifica se o mês está no intervalo de 1 a 12
        if mes < 1 or mes > 12:
            return False

        # Verifica se o dia está no intervalo correto para o mês
        if mes == 2:  # Fevereiro
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                if dia < 1 or dia > 29
                return False
            else:
                if dia < 1 or dia > 28:
                    return False
        elif mes in [4, 6, 9, 11]:  # Abril, Junho, Setembro, Novembro
            if dia < 1 or dia > 30:
                return False
        else:  # Outros meses com 31 dias
            if dia < 1 or dia > 31:
                return False

        # Se todas as verificações passaram, a data é válida
        return True
    except ValueError:
        return False

# Solicita a data ao usuário
data = input("Digite uma data no formato dd/mm/aaaa: ")

# Verifica se a data é válida
if data_valida(data):
    print("A data é válida.")
else:
    print("A data é inválida.")
