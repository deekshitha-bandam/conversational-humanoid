import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pywhatkit
import pyjokes


print('Loading your personal assistant ')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"Your Voice:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


speak("Loading your personal assistant ")
wishMe()

if __name__ == '__main__':

    while True:

        speak("listening")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Thank You your Assistant is now shutting down,Good bye')
            print('your personal assistant is shutting down,Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'name' in statement:

            speak("Personal assistant")
            time.sleep(2)

        elif 'nice to meet you' in statement:

            speak("it's my pleassure")
            time.sleep(2)

        elif 'old' in statement:

            speak("am 2 hours old developed assistant.")
            time.sleep(2)

        elif 'ok' in statement:
            speak("Thank You")

        elif ' social app' in statement:
            speak('which app do you want to open')
            time.sleep(1)
            speak('whatsapp,facebook,twitter,p.projects')
            print('1. whatsapp,2. facebook,3. twitter')

        elif '1' in statement or "whatsapp" in statement:
            webbrowser.open_new_tab("https://web.whatsapp.com/")
            speak("whatsapp is open now")
            time.sleep(5)

        elif '2' in statement or "facebook" in statement:
            webbrowser.open_new_tab("https://www.facebook.com")
            speak("Facebook is open now")
            time.sleep(5)



        elif '3' in statement or "twitter" in statement:
            webbrowser.open_new_tab("https://www.twitter.com")
            speak("Facebook is open now")
            time.sleep(5)



        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'play' in statement:
            song = statement.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'joke' in statement or "make me laugh" in statement:
            speak(pyjokes.get_joke())



        elif 'who are you' in statement or 'what can you do' in statement:
            speak(
                'I am your persoanl assistant. I am programmed to minor tasks like'
                'opening youtube,google chrome,gmail,predict time,take a photo,search wikipedia,predict weather'
                'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')



        elif 'news' in statement or "world" in statement or "update" in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "p.projects camera", "img.jpg")


        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)





        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif 'rest' in statement:
            speak("don't worry i play some music to you ")
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=1ZYbU82GVz4")
            speak("close your eyes and keep this laptop aside")
            time.sleep(3)



        else:
            speak("Sorry i can't reach you")

time.sleep(3)