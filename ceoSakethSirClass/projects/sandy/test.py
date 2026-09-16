'''
gTTS -->Google text to speech
playsound --> pip install playsound==1.2.2
pyaudio -->pip install pyaudio

3 functions-->
1.Listen (SpeechRecognition)
2.respond (gtts)
3.Assistant (conditions) --> Conversation, Greeting, datetime, locate a place, open a browser, play a youtube video

text=gTTS('Hello guys!, how are you doing?')
#text.save('audio.mp3')
playsound.playsound('audio.mp3')
'''

from gtts import gTTS
from twogames import playaGame
from proj6QR_code import qr_code
import qrcode
import playsound
import time
import os
import uuid 
import pyaudio
import speech_recognition as sr
import os
import webbrowser


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source,phrase_time_limit=10)
    data = " "
    try:
        data = r.recognize_google(audio)
        print("You said:",data)
    except:
        print("Sorry, I didn't get that")
    return data.lower()




def respond(String):
    """Function to respond back"""
    print(String)
    tts=gTTS(String)
    tts.save('Speech.mp3')
    #we are using uuid --> to randomize the content in the audio file
    filename="Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def va(data):
    """Our Virtual Assistant with the actions"""
    if "how are you" in data:
        listening=True
        respond('I am fine, thanks for asking')

    elif "fine" in data:
        listening=True
        respond('Thank you')

    elif 'what are your plans' in data:
        listening=True
        respond('Only study... one focus in 2026')

    elif 'how are things going' in data:
        listening=True
        respond('Antha okay ika nene set avvali')
    elif 'time' in data:
        listening=True
        respond(time.ctime())
    elif 'stop talking'  in data:
        listening=True
        respond('Okay cool... kophadakuu bye')
        exit()
    elif "say abcd" in data:
        listening = True
        respond(" a b c d e f g h i j k l m n o p q r s t u v w x y z")
    elif "play game" in data:
        listening = True
        respond("opening game")
        playaGame()

    elif "qr code" in data:
        listening = True
        respond("Opening QR code generator")

        qr_code()

        respond("QR code created successfully")

 
    elif "open youtube" in data:
        listening=True
        respond("opening youtube")
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in data:
        listening=True
        respond("opening google")
        webbrowser.open("https://www.google.com/")
        respond("opened google")


    try:
        return listening
    except UnboundLocalError as e:
        print('Make sure to speak louder and faster')

respond('Hey sandy... Good to hear from you. How are you?')
listening=True
while listening:
    data=listen()
    listening=va(data)

