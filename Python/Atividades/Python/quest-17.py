def par_impar():
    numeros = []
    par = []
    impar = []
    for i in range (7):
        n = int(input(f"Digite o {i+1}° número: "))
        numeros.append(n)
    for p in numeros:
        if p % 2 == 0:
            par.append(p)
        else:
            impar.append(p)
    print(f"{len(par)} são números pares e {len(impar)} são números impares")
par_impar()