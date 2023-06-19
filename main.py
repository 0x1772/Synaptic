import logging
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

# Log dosyasının adı, dizini ve formatı
log_directory = "C:\\Users\\realh\\Masaüstü\\Synaptic\\log_directory\\"
log_file = log_directory + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "-synaptic_app.log"
log_format = "%(asctime)s - %(levelname)s - %(message)s"

# Loglama ayarlarını yapılandırma
logging.basicConfig(filename=log_file, level=logging.INFO, format=log_format)

# GET ARGUMENTS FROM USER
def get_arguments():
    parser = argparse.ArgumentParser()
    optional = parser.add_argument_group("paramets")
    optional.add_argument("-v", "--voice", action="store_true", required=False, help="Enable Voice Mode")
    optional.add_argument("-g", "--googlespeech", action="store_true", required=False, help="enable googlespeech")
    arguments = parser.parse_args()
    return arguments

# GTTS LOGIC
def google_speak(synaptic_speak):
    tts = gTTS(text=synaptic_speak, lang="tr", slow=False)
    date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice" + date_string + ".mp3"
    file_path =  "C:\\Users\\realh\\Masaüstü\\Synaptic\\audio_files\\" + filename  # Dosya yolunu burada değiştirin
    tts.save(file_path)
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)

# FIREFOX
def open_firefox():
    firefox_path = r"C:\Program Files\Firefox Developer Edition\firefox.exe"
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path), 1)
    webbrowser.get('firefox').open('about:blank')
    logging.info("Firefox Developer Edition uygulaması açıldı.")

# COMPUTER HEAT LEVEL
def get_temperature():
    temperature = psutil.sensors_temperatures()['coretemp'][0].current
    return str(temperature)

# OFFLINE SPEAK
def offline_speech(synaptic_speak):
    engine = pyttsx3.init()
    engine.say(synaptic_speak)
    engine.runAndWait()

# ONLINE SPEAK
def online_speech(synaptic_speak):
    if voice == "gTTS":
        google_speak(synaptic_speak)
    else:
        offline_speech(synaptic_speak)

# LISTENER WITH MIC
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        logging.info("Dinleniyor...")
        audio = r.listen(source)
    try:
        spoken_text = r.recognize_google(audio, language="tr")
        logging.info(spoken_text)
        return spoken_text
    except sr.UnknownValueError:
        return listen()
    except sr.RequestError as e:
        error_message = "Veri alınamıyor: Google Speech Recognition servisi; {0}".format(e)
        logging.error(error_message)
        online_speech("Veri alınamıyor, lütfen tekrar deneyin.")
        return listen()

if __name__ == "__main__":
    # Loglama özelleştirmeleri için logger oluşturma
    logger = logging.getLogger("SynapticLog")

    # Loglama seviyesini ayarlama
    logger.setLevel(logging.INFO)

    # Log dosyasına yazma işlemi için bir FileHandler oluşturma
    log_handler = logging.FileHandler(log_file)

    # Log formatını ayarlama
    log_formatter = logging.Formatter(log_format)

    # Log handler'a formatlayıcıyı ve seviyeyi ekleyerek yapılandırma
    log_handler.setFormatter(log_formatter)
    logger.addHandler(log_handler)

    args = get_arguments()
    if args.voice:
        try:
            mode = "voice"
        except ImportError:
            logger.warning("speech_recognition modülü yüklenmedi. Metin moduyla başlatılıyor.")

    if args.googlespeech:
        try:
            voice = "gTTS"
        except ImportError:
            logger.warning("pyttsx3 modülü yüklenmedi. pyttsx3 kullanılıyor.")

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
        logging.info("Synaptic: " + synaptic_speak)
        online_speech(synaptic_speak)
        
class Synaptic:

    def __init__(self):
        self.packages = []

    def get_packages(self):
        return self.packages

    def install_package(self, package_name):
        self.packages.append(package_name)

    def uninstall_package(self, package_name):
        self.packages.remove(package_name)
