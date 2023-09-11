# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('digite uma letra: '))

# Convertemos a letra para minúscula usando o método lower() para facilitar a comparação.
if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
    print('a letra é uma vogal')
else:
    print("A letra é uma consoante.")