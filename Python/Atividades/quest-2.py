print("Saiba se você tem direito à disconto já")
def Desconto():
    valor = float(input("Diga o valor do produto que desejas comprar: "))
    if valor > 100:
        valor_final = valor*0.9
        print(f"O valor com desconto é {valor_final}")
    else:
        print("Você não tem direito à desconto")

Desconto()