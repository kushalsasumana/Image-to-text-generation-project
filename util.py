from gtts import gTTS
import os
import main
lan='en'
myfile = open("recognized_"+str(main.count-1)+".txt", "rt") # open recognized_current count.txt for reading text
contents = myfile.read()         # read the entire file to string
myfile.close()                   # close the file
text=print(contents)
speech=gTTS(text=text,lang=lan, slow=False,tld="co.in")
speech.save("TTS1.mp3")
os.system("TTS1.mp3")