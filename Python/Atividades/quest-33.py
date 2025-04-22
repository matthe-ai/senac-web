from datetime import datetime

def agenda_digital():
    print("Bem vindo à agenda digital")
    data = datetime.now()
    print(f"Hoje é dia {data.strftime("%d/%m/%Y")} e agora são {data.strftime("%H:%M")}")
    resp = input("Você deseja agendar um compromisso ? (s) (n) ")
    if resp.lower() == "s":
        evento = input("Qual o nome do evento ? ")
        evento_d = input("Qual a data do evento ? (Apenas data separada por / ) ")
        print(evento, evento_d)
agenda_digital()