import requests
from win32com.client import Dispatch

def speak(str):
       voice = Dispatch('SAPI.SpVoice')
       voice.speak(str)
def headlines():
       data = requests.get('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=3dfea29fe4ac4114b23c82f3b3ad75be')
       alldata = data.json()
       articles = alldata['articles']
       for i in range(1,11):
              a = articles[i]['description']
              print(a)
              speak(f'news number{i} . {a}')

speak("Hello .  welcome to news1 news centre ")
speak("here are the headlines ")
headlines()
speak(" . thank you for listening")
