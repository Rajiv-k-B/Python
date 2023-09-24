import speech_recognition as sr

AUDIO_FILE = ("Recording.wav")

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
    
#reads the audio file


try:
    print("audio file contains "+r.recognize_google(audio))
except sr.UnkownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError:
    print("Could't get result from Google Speech Recognition")