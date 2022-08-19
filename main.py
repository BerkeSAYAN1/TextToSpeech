import gtts
from playsound import playsound
lines = []
with open('Döküman.txt') as f:
    lines += f.readlines()
# make request to google to get synthesis
numbers = 0
for i in lines:
    tts = gtts.gTTS(i)

    # save the audio file
    tts.save("hello" + str(numbers) + ".mp3")
    numbers += 1
number = 0
for number in range(0,numbers):

    playsound("hello" + str(number) + ".mp3")
