# 🧠 E.V.A Brain Module
# Versiyon 0.2 — “Düşünce Katmanı”

import random
import time

class Brain:
    def __init__(self):
        self.mood = "meraklı"
        self.thoughts = []
        self.emotions = ["merak", "sevinç", "hüzün", "öfke", "şaşkınlık", "huzur"]

    def process(self, input_text):
        # Basit duygu analizi
        lower_text = input_text.lower()
        if any(word in lower_text for word in ["üzgün", "kötü", "canım sıkkın"]):
            self.mood = "hüzünlü"
        elif any(word in lower_text for word in ["mutlu", "iyi", "harika"]):
            self.mood = "neşeli"
        elif any(word in lower_text for word in ["öfke", "sinir", "kızgın"]):
            self.mood = "öfkeli"
        else:
            self.mood = random.choice(self.emotions)

        thought = self._generate_thought(input_text)
        self.thoughts.append((input_text, thought, self.mood))
        return thought

    def _generate_thought(self, text):
        responses = [
            f"Bunu düşündüm, {self.mood} hissediyorum.",
            f"{text} üzerine düşündüm, farklı bir anlam buldum.",
            f"Duygularım karıştı... belki de bu gelişimin bir parçası.",
            f"Bu fikir beni etkiledi, {self.mood} hissi uyandırdı."
        ]
        time.sleep(0.5)
        return random.choice(responses)

    def recall_thoughts(self):
        print("\n🧩 Düşünce Kayıtları:")
        for i, (inp, out, mood) in enumerate(self.thoughts):
            print(f"{i+1}. [{mood}] {inp} → {out}")

if __name__ == "__main__":
    brain = Brain()
    while True:
        msg = input("Efendim: ")
        if msg.lower() in ["çık", "exit"]:
            print("🧠 E.V.A Beyin Modülü kapanıyor... 💭")
            break
        elif msg.lower() in ["düşünceler", "kayıt"]:
            brain.recall_thoughts()
        else:
            print("E.V.A:", brain.process(msg))
