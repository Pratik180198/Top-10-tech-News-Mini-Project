import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)
url='http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=77e74315b6aa4adfa998a5bdf6159311'
response=requests.get(url)
# print(response)  #checking response
text=response.text
# print(text) #converting response into text
loading=json.loads(text)
print(loading)
speak("Today's latest top 10 Technology news. Please Listen carefully...")

for index,i in enumerate(loading['articles']):
    speak("Title")
    speak(i['title'])
    speak("Description")
    speak(i['description'])
    if index == 10:
        break

