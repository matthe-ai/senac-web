def caracter_unico():
    frases = set()
    frase = input("Digite uma frase: ")
    frases.update(frase)
    print(f"Existem {len(frases)} caracteres diferentes")
    print(f"Esses caracteres são: {frases}")
caracter_unico()