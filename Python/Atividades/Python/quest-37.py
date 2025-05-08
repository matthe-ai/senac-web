import calendar

def dia_da_semana():
    ano = int(input("Digite o ano: "))
    mes = int(input("Digite o mês: "))
    dia = int(input("Digite o dia: "))
    semana = calendar.weekday(ano,mes,dia)
    match semana:
        case 0:
            print(f"O dia da semana da data {dia}/{mes}/{ano} é segunda-feira")
        case 1:
            print(f"O dia da semana da data {dia}/{mes}/{ano} é terça-feira")
        case 2:
            print(f"O dia da semana da data {dia}/{mes}/{ano} é quarta-feira")
        case 3:
            print(f"O dia da semana da data {dia}/{mes}/{ano} é quinta-feira")
        case 4:
            print(f"O dia da semana da data {dia}/{mes}/{ano} é sexta-feira")
        case 5:
            print(f"O dia da semana da data {dia}/{mes}/{ano} é sábado")
        case 6:
            print(f"O dia da semana da data {dia}/{mes}/{ano} é domingo")
dia_da_semana()