# IMPORT LIBRARIES for Project
import aiml
import os
import time
import argparse
import pyttsx3

mode = "text"
voice = "pyttsx"
terminate = ["bye", "quit","by","bb","goodbye","good bye","see you later","seeyoulater","off",]

# GET ARGUMENTS FROM USER
def get_arguments():
    parser = argparse.ArgumentParser()
    optional = parser.add_argument_group("paramets")
    optional.add_argument("-v", "--voice", action = "store_true", required = False, help = "enable voice")
    optional.add_argument("-g", "--googlespeech", action = "store_true", required = False, help = "enable googlespeech")
    arguments = parser.parse_args()
    return arguments

def google_speak(synaptic_speak):
    tts = gTTS(text = synaptic_speak, lang = "tr")
    tts.save("audio.mp3")
    mixer.init()
    mixer.music.load("audio.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(2)

def offline_speech(synaptic_speak):
    engine = pyttsx3.init()
    engine.say(synaptic_speak)
    engine.runAndWait()
    
def online_speech(synaptic_speak):
    if(voice == "gTTS"):
        gtts_speak(synaptic_speak)
    else:
        offline_speech(synaptic_speak)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        speech = r.recognize_google(audio)
        print("You said: " + speech)
        return speech
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return 0
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return 0
    
if __name__ == "__main__":
    args = get_arguments()
    if(args.voice):
        try:
            import speech_recognition as sr
            mode = "voice"
        
        except ImportError:
            print("\nInstall speech_recognition to use this feature" + "\nStarting text mode")
    
    if(args.googlespeech):
        try:
            from gtts import gTTS
            from pygame import mixer
            voice = "gTTS"
        
        except ImportError:
            import pyttsx
            print("\n Please install pyttsx to use this feature" + "\nUseing pyttsx ")
    
    else:
        import pyttsx3
        
    kernel = aiml.Kernel()
    if os.path.isfile("bot_brain.brn"):
        kernel.bootstrap(brainFile = "bot_brain.brn")
    else:
        kernel.bootstrap(learnFiles = "std-startup.xml", commands = "LOAD AIML B") 
    
    while True:
        if mode == "voice":
            response = listen()
        else:
            response = input("Enter The Message:  ")
        if response.lower().replace(" ", "") in terminate: 
            break
        synaptic_speak = kernel.respond(response)
        print("synaptic: " + synaptic_speak )
        google_speak(synaptic_speak)