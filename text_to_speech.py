import gtts
print("\033[0;30;46mPlease read the description")
def tts(text):
    gtts.gTTS(text,lang="en").save("voiceOutput.mp3")
    print("File saved as: voiceOutput.mp3")
