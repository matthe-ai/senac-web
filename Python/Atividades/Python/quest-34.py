import time

def temporizador():
    tempo = int(input("Digite quantos segundos é para cronometrar: "))
    for i in range(tempo, -1, -1):
        print(i)
        if i == 0:
            print("Tempo encerrado")
        time.sleep(1)
temporizador()