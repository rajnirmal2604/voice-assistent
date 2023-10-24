import pyttsx3 #text to speech converter 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib #for email
import time


engine = pyttsx3.init('sapi5') #here sapi5 is use to take inbuilt window voice for male=0 and female=1
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait() #audible to us

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

speak("I am your assistant. Please tell me how may I help you?")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        r.adjust_for_ambient_noise(source)   #noise reduction
        audio = r.listen(source)
        

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e: 
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vishwamevawala@gmail.com', '  Vishwa@341')
    server.sendmail('vishwamevawala20@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    # query = takeCommand().lower()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'exit' in query:
            speak("thank you for giving me your time")
            break
    
        elif 'open vs code' in query:
            codePath = "C:\\Users\\Vishwa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vishwamevawala20@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry.I am not able to send this email") 

        elif 'tell my boyfriend name' in query:
            speak("try after you get the job !!!!focus on your goal.")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' or 'good' in query:
            speak("Good to know that you are fine")

        elif 'who made you' in query:
            speak("I have been created by dhruv and vishwa")

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")		
            webbrowser.open(query)

        elif 'who are you' in query:
            speak("I am your virtual assistant created by nirma university student")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop your assistant from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('text.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
            
        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            os.system("shutdown /s /t 30")
		