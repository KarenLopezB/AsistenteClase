import speech_recognition as sr
import time
import webbrowser
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexa_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            alexa_speak('Lo siento, no te entendi')
        except sr.RequestError:
            alexa_speak('Lo siento, error de conexion')
        return voice_data

def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang='es') 
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'como te llamas' in voice_data:
        alexa_speak('Mi nombre es alexa')
    if 'time' in voice_data:
        alexa_speak(ctime())
    if 'buscar' in voice_data:
        buscar = record_audio('¿Qué necesitas buscar?')
        url = 'https://google.com/search?q=' + buscar
        webbrowser.get().open(url)
        alexa_speak('Esto es lo que encontre para: ' + buscar )
    if 'place' in voice_data:
        lugar = record_audio('¿Qué lugar?')
        url = 'https://google.nl/maps/place/' + lugar + '/&amp;'
        webbrowser.get().open(url)
        alexa_speak('Esto es lo que encontre para: ' + lugar )
    if 'color' in voice_data:
        color = record_audio('¿Qué color buscas?')
        url = 'https://google.com/search?q=' + color
        webbrowser.get().open(url)
        alexa_speak('Esto es lo que encontre para: ' + color )
    if 'video' in voice_data:
        video = record_audio('¿Qué video buscas?')
        url = 'https://www.youtube.mx/' + video 
        webbrowser.get().open(url)
        alexa_speak('Esto es lo que encontre para: ' + video )
    if 'clima' in voice_data:
        clima = record_audio()
        url = 'https://www.google.com/search?q=clima' + clima
        webbrowser.get().open(url)
    if 'noticias' in voice_data:
        noticias = record_audio()
        url = 'https://news.google.com/' + noticias
        webbrowser.get().open(url)
        alexa_speak('Estas son las noticias de hoy: ' + noticias )
    if 'exit' in voice_data:
        exit()


time.sleep(1)
alexa_speak('¿Cómo te puedo ayudar?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
    print(voice_data)