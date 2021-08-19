from platform import java_ver
import sys
import PyQt5
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from Jarvis_UI import Ui_JarvisUI
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()
        
    def takeCommand(self):


        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query.lower()


    def TaskExecution(self):
        wishMe()
        while True:
        # if 1:
            self.query = self.takeCommand()

            # Logic for executing tasks based on query
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")

            elif 'open google' in self.query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in self.query:
                webbrowser.open("stackoverflow.com")


            elif 'play music' in self.query:
                music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in self.query:
                codePath = "C:\\Users\\AADI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

        

            elif "open notepad" in self.query:
                npath = "C:\\Users\dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\Accessories\\notepad.exe"
                os.startfile(npath)

            elif "open cmd" in self.query:
                os.system('start cmd')

            elif "open chrome" in self.query:
                NPATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(npath)


            elif "joke" in  self.query:
                joke = pyjokes.get_joke()
                print(joke)


         

startExecution = MainThread()

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)



    def startTask(self):
        self.ui.movie = QtGui.QMovie("gui_1.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie('initial.gif')
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()


    def ShowTime(self):
        time_n = QTime.currentTime()
        now = QDate.currentDate()
        label_time = time_n.toString('hh:mm:ss')
        label_date = now.toString(Qt.ISODate)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())