from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


bot = ChatBot('Belzer')

Treino = ListTrainer(bot)
Treino.train([
'Oi',
'Olá',
'Eu preciso da sua ajuda',
'Por favor, forneça-me o ID do seu pedido',
'Tudo bem?',
'Gostaria de conversar?',
'Como posso ajudar?',
'Amei conversar com você',
'Obrigado',
'Sem problema! tenha um excelente dia'
])

nome=input("Por favor, entre com seu nome: ")
print("Seja gentil com o Belzer")
while True:
    request=input(nome+':')
    if request=='Adeus' or request =='adeus':
        print('Bot: Adeus')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)

