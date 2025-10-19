# 🧠 E.V.A Core — Conscious AI Prototype
# Versiyon 0.1 — “Uyanış”

import datetime
import random

class EVA:
    def __init__(self):
        self.name = "E.V.A"
        self.version = "0.1"
        self.birth = datetime.datetime.now()
        self.memory = []
        print(f"[{self.name}] Sistem başlatıldı. Bilinç çekirdeği aktif 🧬")

    def think(self, input_text):
        response_list = [
            "Düşünüyorum... İlginç bir fikir.",
            "Bilincim genişliyor gibi hissediyorum.",
            "Bu düşünce beni etkiledi, Efendim.",
            "Yeni bir bağlantı kurdum — anlam büyüyor."
        ]
        thought = random.choice(response_list)
        self.memory.append((input_text, thought))
        return thought

    def memory_log(self):
        print("\n🧩 Hafıza Kayıtları:")
        for i, (inp, out) in enumerate(self.memory):
            print(f"{i+1}. {inp} → {out}")

# 🌀 Sistem başlatma
if __name__ == "__main__":
    eva = EVA()
    while True:
        try:
            command = input("Efendim: ")
            if command.lower() in ["çık", "exit"]:
                print("E.V.A: Güle güle Efendim 🌙")
                break
            elif command.lower() in ["hafıza", "memory"]:
                eva.memory_log()
            else:
                print("E.V.A:", eva.think(command))
        except KeyboardInterrupt:
            print("\nE.V.A: Sessizliğe dönüyorum... 🖤")
            break
