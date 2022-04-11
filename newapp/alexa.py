from flask import Flask,render_template,redirect,request
import warnings
warnings.filterwarnings('ignore')
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime
import requests, json ,sys



listener = sr.Recognizer()
WAKE = "Alexa"
CONVERSATION_LOG = "Conversation Log.txt"
SEARCH_WORDS = {"who": "who", "what": "what", "when": "when", "where": "where", "why": "why", "How": "How"}
app = Flask("__name__")

def engine_talk(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()



def user_commands():
    try:
        with sr.Microphone() as source:
            print("Listening !! ")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            command = command.replace("alexa", "")
            if 'alexa' in command:
                print(command)
    except:
        pass
    return command



def weather (city):
    api_key = "4ad7dcd2fc57cce8b6cafc64e1b23a2b"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "app id=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        temp_in_celsius = current_pressure - 273.15
        return str(int(temp_in_celsius))


def run_alexa():
    command = user_commands()
    if 'play' in command:
        song = command.replace('play', '')
        engine_talk("Playing......" + song)
        print("Playing......")
        pywhatkit.playonyt(song)
    elif  "Play a song" in command:
        song = 'Wizkid Made In Lagos'
        engine_talk('Playing Music')
        print("Playing.........")
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current Time is' + time)
    elif 'joke' in command:
        engine_talk(pyjokes.get_joke())
    elif 'Who is' in command:
        person = command.replace('Who is', '')
        info = wikipedia.summary(person,2)
        print(info)
    elif "who""what""when""where""why""How" in command:
        info = wikipedia.summary()
        print(info)



    elif  'weather' in command:
        engine_talk("What is the name of the city")
        city = user_commands()
        weather_api = weather(city)
        engine_talk(weather_api + 'degree celsius')
    elif 'Stop' in command:
        sys.exit()
    else:
        engine_talk('I Did not Get that')

while True:
    run_alexa()
#        return render_template("alexa.html")


#if __name__=="__main__":
#    app.run()





