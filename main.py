import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from datetime import date
import requests

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hey computer' in command:
                command = command.replace('hey computer', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'date' in command:
        date_today = datetime.datetime.now().strftime("%B %d, %Y")
        talk("Today's date is" + date_today)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is an' in command:
        thing = command.replace('what is an', '')
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)
    elif 'what is a' in command:
        thing = command.replace('what is a', '')
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        thing = command.replace('what is', '')
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)
    elif 'what are' in command:
        thing = command.replace('what are', '')
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif '9 + 10' in command:
        print(21)
        talk(21)
    elif 'thank you' in command:
        print("I am glad i could assist you today.")
        talk("I am glad i could assist you today.")
    elif 'thanks' in command:
        print("I am glad i could assist you today.")
        talk("I am glad i could assist you today.")
    else:
        talk('I didnt quite catch that, could you repeat it?')


while True:
    run_alexa()