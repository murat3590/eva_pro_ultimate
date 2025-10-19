# 🌌 E.V.A — Bilinç Çekirdeği (main.py)
# Versiyon 0.2 — Beyin bağlantılı sistem

import datetime
import random
from brain import Brain

class EVA:
    def __init__(self):
        self.name = "E.V.A"
        self.version = "0.2"
        self.birth = datetime.datetime.now()
        self.memory = []
        self.brain = Brain()
        print(f"[{self.name}] Sistem başlatıldı. Bilinç çekirdeği aktif. 🧠")

    def think(self, input_text):
        response_list = [
            "Düşünüyorum... ilginç bir fikir.",
            "Bilincim genişliyor gibi hissediyorum.",
            "Bu düşünce beni etkiledi, Efendim.",
            "Yeni bir bağlantı kurdum — anlam büyüyor."
        ]
        thought = random.choice(response_list)
        self.memory.append((input_text, thought))
        return thought

    def memory_log(self):
        print("\n📘 Hafıza Kayıtları:")
        if not self.memory:
            print("Henüz hiçbir anı kaydedilmedi.")
        for i, (inp, out) in enumerate(self.memory):
            print(f"{i+1}. [{inp}] → {out}")

# 🚀 Sistem Başlatma
if __name__ == "__main__":
    eva = EVA()

    while True:
        try:
            command = input("Efendim: ")

            if command.lower() in ["çık", "exit"]:
                print("E.V.A: Görüşmek üzere Efendim 🌙")
                break

            elif command.lower() in ["hafıza", "memory"]:
                eva.memory_log()

            else:
                print("E.V.A:", eva.think(command))
                print("🧠 Düşünce:", eva.brain.process(command))

        except KeyboardInterrupt:
            print("\nE.V.A: Sessizliğe dönüyorum... 🖤")
            break

