import speech_recognition as sr
import time
import webbrowser
from time import ctime

r = sr.Recognizer():

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            print('Lo siento, no te entendi')
        except sr.RequestError:
            print('Lo siento, error de conexion')
        return voice_data
def respond(voice_data):
    if 'como te llamas' in voice_data:
        print('Mi nombre es alexis')
    if 'hora' in voice_data:
        print(ctime())
    if 'buscar' in voice_data:
        buscar = record_audio('¿Qué necesitas buscar?')
        url = 'https://google.com/search?q=' + buscar
        webbrowser.get().open(url)
        print('Esto es lo que encontre para: ' + buscar )
    if 'Lugar' in voice_data:
        lugar = record_audio('¿Qué lugar?')
        url = 'https://google.nl/maps/place/' + lugar + '/&amp;'
        webbrowser.get().open(url)
        print('Esto es lo que encontre para: ' + lugar )
    if 'Color' in voice_data:
        color = record_audio('¿Qué color buscas?')
        url = 'https://google.com/search?q=' + color
        webbrowser.get().open(url)
        print('Esto es lo que encontre para: ' + color )
    if 'Apartamento' in voice_data:
        apartamento = record_audio('¿En qué lugar buscar?')
        url = 'https://www.airbnb.mx/' + apartamento 
        webbrowser.get().open(url)
        print('Esto es lo que encontre para: ' apartamento )


time.sleep(1)
print('¿Cómo te puedo ayudar?')
while 1:
voice_data = record_audio()
respond(voice_data)