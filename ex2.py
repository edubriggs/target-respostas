"""
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
"""
c_letras = 0

letras_a = 'aáàâãAÁÀÂÃ'

texto = input("Digite a palavra desejada: ")

for palavra in texto:
    if palavra in letras_a:
        c_letras += 1

if c_letras > 1:
    print(f"A palavra {texto} tem {c_letras} letras A's nela")
else:
    print(f"A palavra {texto} não tem nenhuma letra A nela")