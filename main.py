import gtts
from playsound import playsound
lines = []
with open('Döküman.txt') as f:
    lines += f.readlines()
# make request to google to get synthesis
tts = gtts.gTTS(lines[0])

# save the audio file
tts.save("hello.mp3")

playsound("hello.mp3")
