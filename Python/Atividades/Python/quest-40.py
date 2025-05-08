import emoji
from datetime import datetime

def emojes_chat():
    hora = datetime.now()
    hora = int(hora.strftime("%H"))
    if hora < 12:
        print(emoji.emojize("Bom dia :sun:"))
    elif hora < 18 and hora > 12:
        print(emoji.emojize("Boa tarde :sun_behind_cloud:"))
    else:
        print(emoji.emojize("Boa noite :full_moon:"))
emojes_chat()