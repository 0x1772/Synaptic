# IMPORT LIBRARIES for Project
import aiml
import os
import time
import argparse
import pyttsx3
from gtts import gTTS
from pygame import mixer
import speech_recognition as sr

mode = "text"
voice = "pyttsx"
terminate = ["bye", "quit", "by", "bb", "goodbye", "good bye", "see you later", "seeyoulater", "off"]

# GET ARGUMENTS FROM USER
def get_arguments():
    parser = argparse.ArgumentParser()
    optional = parser.add_argument_group("paramets")
    optional.add_argument("-v", "--voice", action="store_true", required=False, help="enable voice")
    optional.add_argument("-g", "--googlespeech", action="store_true", required=False, help="enable googlespeech")
    arguments = parser.parse_args()
    return arguments

def google_speak(synaptic_speak, speed=1.0):
    tts = gTTS(text=synaptic_speak, lang="tr")
    tts.save("audio.mp3")

    sound = AudioSegment.from_file("audio.mp3")
    modified_sound = sound.speedup(playback_speed=speed)
    modified_sound.export("audio.mp3", format="mp3")

    mixer.init()
    mixer.music.load("audio.mp3")
    mixer.music.play()

    while mixer.music.get_busy():
        time.sleep(1)

def offline_speak(synaptic_speak):
    engine = pyttsx3.init()
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Konuşma hızı (isteğe bağlı)
    engine.setProperty('volume', 0.8)  # Ses seviyesi (isteğe bağlı)
    engine.setProperty('voice', 'tr')  # Türkçe seslendirme için 'tr' kullanılır
    engine.say(synaptic_speak)
    engine.runAndWait()

def online_speech(synaptic_speak):
    if voice == "gTTS":
        google_speak(synaptic_speak)
    else:
        offline_speak(synaptic_speak)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print(r.recognize_google(audio))
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        online_speech("Ne dediğinizi anlayamadım, lütfen tekrar eder misiniz?")
        return listen()
    except sr.RequestError as e:
        print("Veri alınamıyor: Google Speech Recognition servisi; {0}".format(e))

if __name__ == "__main__":
    args = get_arguments()
    if args.voice:
        try:
            mode = "voice"
        except ImportError:
            print("\nspeech_recognition'ı kullanmak için yükleyin" + "\nMetin moduyla başlatılıyor.")

    if args.googlespeech:
        try:
            voice = "gTTS"
        except ImportError:
            print("\nLütfen 'pyttsx3'ü yükleyin" + "\npyttsx3 kullanılıyor.")

    kernel = aiml.Kernel()
    if os.path.isfile("bot_brain.brn"):
        kernel.bootstrap(brainFile="bot_brain.brn")
    else:
        kernel.bootstrap(learnFiles="std-startup.xml", commands="LOAD AIML B")

    while True:
        if mode == "voice":
            response = listen()
        else:
            response = input("Enter The Message: ")
        if response.lower().replace(" ", "") in terminate:
            break
        synaptic_speak = kernel.respond(response)
        print("Synaptic: " + synaptic_speak)
        online_speech(synaptic_speak)
