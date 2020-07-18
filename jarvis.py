import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia # pip install wikipedia
import smtplib
import webbrowser as wb 
import os
import pyautogui # pip install pyautogui
import psutil # pip install psutil
import pyjokes # pip install pyjokes
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)

def hour():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning")
    elif  hour >= 12 and hour< 18:
        speak("Good Afternoon")
    elif  hour >= 18 and hour< 24:
        speak("Good Evening")
    else:
        speak("Good Night")

    speak(hour)

def wishme():
    speak("Welcome back")
    hour()
    speak("Hi, Jarvis at your service. Please tell me how can i help you?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source, phrase_time_limit = 5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
        speak("Did you just say " + query)
    
    except Exception as e:
        print(e)
        speak("Say that again please.....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Sender's Email id', 'APP Password')
    server.sendmail('Sender's Email id',to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\DELL\\Desktop\\Open-cv\\jarvis\\Screenshots\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak('Your device battery percentage is')
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'time' in query:
            time()  

        elif 'date' in query:
            date()

        elif 'thank' in query:
            speak("You are welcome!")

        elif 'wikipedia' in query:
            speak("Searching")
            query = ("wikipedia","")
            result = wikipedia.summary(f'{query}', sentences=2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takecommand()
                to = 'Reciver's E-mail id'
                sendEmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                print(e)
                speak("unable to send email")

        elif 'search in chrome' in query:
            speak("What do you want to search?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
        
        elif 'log out' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            speak("Which song to play?")
            songs_dir = 'E:/songs'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember' in query:
            speak("What do you want me to remember?")
            data = takecommand()
            speak("You said me to remember that " + data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know' in query:
            remember = open('data.txt','r')
            speak("You told me to remember that " + remember.read())
        
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")

        elif 'cpu' in query:
            cpu()

        elif 'jokes' in query:
            jokes()

        elif 'offline' in query:
            speak("Have a nice day")
            quit()
