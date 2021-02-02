from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import speech_recognition as sr
from gtts import gTTS, lang
from playsound import playsound

def ouvir_microfone():
    microfone = sr.recognize()
    with sr.Microphone() as source:
        microfone.adjust_for_ambiente_noice(source)
        print("Microfone...")
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print("Humano: " + frase)
    except sr.UnknownValueError:
        print('bot: Isso não funcionou')
    return frase

def cria_audio(audio):
    tts = gTTS(audio, lang="pt-BR")
    tts.save('bot.mp3')
    playsound('bot.mp3')


bot = ChatBot('Belzer')

BatePapo = [
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
]


Treino = ListTrainer(bot)
Treino.train(BatePapo)


while True: 
    quest = ouvir_microfone()
    resposta = bot.get_response(quest)
    cria_audio(str(resposta))
    print('Bot: ', resposta)

