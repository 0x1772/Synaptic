# IMPORT LIBRARIES for Project
import datetime
import aiml
import os
import time
import argparse
import pyttsx3
from gtts import gTTS
from pygame import mixer
import speech_recognition as sr
import pyaudio
import psutil

mode = "text"
voice = "pyttsx"
terminate = ["bye", "quit", "by", "bb", "goodbye", "good bye", "see you later", "seeyoulater", "off"]

# GET ARGUMENTS FROM USER
def get_arguments():
    parser = argparse.ArgumentParser()
    optional = parser.add_argument_group("paramets")
    optional.add_argument("-v", "--voice", action="store_true", required=False, help="Enable Voice Mode")
    optional.add_argument("-g", "--googlespeech", action="store_true", required=False, help="enable googlespeech")
    arguments = parser.parse_args()
    return arguments

def google_speak(synaptic_speak):
    tts = gTTS(text=synaptic_speak, lang="tr", slow=False)
    date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice" + date_string + ".mp3"
    file_path =  "C:\\Users\\realh\Masaüstü\\Synaptic\\audio_files\\" + filename  # Dosya yolunu burada değiştirin
    tts.save(file_path)
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)
        
# Firefox açan kod        
def open_firefox():
    firefox_path = r"C:\Program Files\Firefox Developer Edition\firefox.exe"
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path), 1)
    webbrowser.get('firefox').open('about:blank')
    print("Firefox Developer Edition uygulaması açıldı.")

# Bilgisayar sıcaklık değerini alma
def get_temperature():
    temperature = psutil.sensors_temperatures()['coretemp'][0].current
    return str(temperature)

        
def offline_speech(synaptic_speak):
    engine = pyttsx3.init()
    engine.say(synaptic_speak)
    engine.runAndWait()

def online_speech(synaptic_speak):
    if voice == "gTTS":
        google_speak(synaptic_speak)
    else:
        offline_speech(synaptic_speak)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinleniyor...")
        audio = r.listen(source)
    try:
        print(r.recognize_google(audio, language="tr"))
        return r.recognize_google(audio, language="tr")
    except sr.UnknownValueError:
        online_speech("Ne dediğinizi anlayamadım, lütfen tekrar eder misiniz?")
        return listen()
    except sr.RequestError as e:
        print("Veri alınamıyor: Google Speech Recognition servisi; {0}".format(e))
        online_speech("Veri alınamıyor, lütfen tekrar deneyin.")
        return listen()


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
