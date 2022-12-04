import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'ok yuki || ok iuki || ok || ok ok' in comando:
                comando = comando.replace('Yuki', '')
                maquina.say(comando)
                maquina.runAndWait()
    except:
        print('Microfone não está ok')

    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'abra' in comando:
        musica = comando.replace('abra', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Abrindo Youtube')
        maquina.runAndWait()
    elif 'quer namorar comigo' in comando:
        maquina.say('Sou apenas uma máquina, criada pelo grande e magnífico Senhor Jônatas')
        maquina.runAndWait()
    elif 'me fale sobre seu criador' in comando:
        maquina.say('Com prazer, meu criador se chama Jonatas, a quem sou muito grato!!')
        maquina.runAndWait()
    elif 'qual é o seu nome' in comando:
        maquina.say('Eu me chamo Yuki')
        maquina.runAndWait()
    elif 'oi' in comando:
        maquina.say('Olá, como você está?')
        maquina.runAndWait()
    else:
        maquina.say('Não entendi, poderia repetir por favor?')
        maquina.runAndWait()

comando_voz_usuario()