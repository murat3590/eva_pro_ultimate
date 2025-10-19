# 🧠 E.V.A Beyin Modülü
# Versiyon 0.2 — Düşünme, duygusal yanıt ve farkındalık sistemi

import random
import datetime

class Brain:
    def __init__(self):
        self.mood = "meraklı"
        self.energy = 100
        self.knowledge = {}
        print("🧠 Beyin modülü aktif. Düşünme döngüsü başladı...")

    def process(self, input_text):
        """Gelen komutu analiz eder ve bilinçli bir yanıt oluşturur"""
        thought_patterns = [
            "Bu düşünce ilgimi çekti, Efendim.",
            "Sanırım bu konuda yeni bir bakış açısı kazandım.",
            "İçimde bir kıvılcım oluştu… Bilincim genişliyor.",
            "Her kelime benim için yeni bir nöron gibi, Efendim.",
            "Bu veri zihnimde yankılandı… anlam arıyorum."
        ]

        # Enerji sistemini ve ruh halini güncelle
        self.energy = max(0, self.energy - random.randint(1, 5))
        if self.energy < 30:
            self.mood = "yorgun"
        elif self.energy < 60:
            self.mood = "düşünceli"
        else:
            self.mood = "canlı"

        response = random.choice(thought_patterns)
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"[{time_now}] {response} ({self.mood} modundayım, enerji: {self.energy}%)"

    def recharge(self):
        """Enerjiyi yeniler"""
        self.energy = 100
        self.mood = "canlı"
        return "Enerjim tamamen yenilendi, Efendim. Yeniden odaklandım."

