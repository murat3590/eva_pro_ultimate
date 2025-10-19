# 🎙️ E.V.A Speech Modülü
# Versiyon 0.1 — Ses sentezi ve algılama

import os
import speech_recognition as sr
import pyttsx3

class SpeechSystem:
    def __init__(self):
        # Konuşma motoru ayarları
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 175)
        self.engine.setProperty('volume', 1.0)
        voices = self.engine.getProperty('voices')
        if voices:
            self.engine.setProperty('voice', voices[0].id)
        print("🎤 E.V.A Ses sistemi başlatıldı.")

        # Dinleme modülü
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def speak(self, text):
        print(f"E.V.A (Ses): {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with self.microphone as source:
            print("🎧 Dinliyorum Efendim...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            command = self.recognizer.recognize_google(audio, language="tr-TR")
            print(f"🗣️ Anladım: {command}")
            return command
        except sr.UnknownValueError:
            self.speak("Üzgünüm Efendim, anlayamadım.")
            return ""
        except sr.RequestError:
            self.speak("Bağlantı hatası, sistem çevrimdışı olabilir.")
            return ""
