"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

# def = declara uma função
# A função saudacao(turno) recebe o turno como argumento e retorna uma mensagem de saudação de acordo com o turno informado.
def saudacao(turno):
    if turno == 'M':
        return "Bom Dia!"
    elif turno == 'V':
        return "Boa Tarde!"
    elif turno == 'N':
        return "Boa Noite!"
    else:
        return "Valor Inválido!"

# Na função main(), solicitamos ao usuário que digite o turno e convertemos a entrada para letras maiúsculas usando o método upper() para garantir que seja case-insensitive.
def main():
    turno = input("Em que turno você estuda? Digite M-matutino ou V-Vespertino ou N-Noturno: ").upper()
    mensagem = saudacao(turno)
    print(mensagem)

# Em seguida, chamamos a função saudacao(turno) com o valor inserido pelo usuário e armazenamos o resultado na variável mensagem.
if __name__ == "__main__":
    main()

