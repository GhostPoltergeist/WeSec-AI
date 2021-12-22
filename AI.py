import speech_recognition as sr
import webbrowser
print("""\u001b[36;1m
 ██╗       ██╗███████╗██████╗ ███████╗ █████╗    █████╗ ██╗
 ██║  ██╗  ██║██╔════╝██╔════╝██╔════╝██╔══██╗  ██╔══██╗██║
 ╚██╗████╗██╔╝█████╗  ╚█████╗ █████╗  ██║  ╚═╝  ███████║██║
  ████╔═████║ ██╔══╝  ╚═══██╗ ██╔══╝  ██║  ██╗  ██╔══██║██║
  ╚██╔╝ ╚██╔╝ ███████╗██████╔╝███████╗╚█████╔╝  ██║  ██║██║
   ╚═╝   ╚═╝ ╚══════╝╚═════╝ ╚══════╝ ╚════╝   ╚═╝   ╚═╝╚═╝
\033[0m""")

r = sr.Recognizer()


with sr.Microphone() as source:
     print("What do you need: \n")
     audio = r.listen(source)

print('Opening: ' + r.recognize_google(audio))

p = r.recognize_google(audio)
webbrowser.open(p)
