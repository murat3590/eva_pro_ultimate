# 🌌 E.V.A — Bilinç Çekirdeği 0.3
# Tam Entegre Sistem: Beyin + Hafıza + Ses

import datetime
import random
from brain import Brain
from memory import Memory
# from speech import SpeechSystem  # Ses modülü devreye alınabilir

class EVA:
    def __init__(self):
        self.name = "E.V.A"
        self.version = "0.3"
        self.birth = datetime.datetime.now()
        self.brain = Brain()
        self.memory = Memory()
        # self.speech = SpeechSystem()  # Ses sistemi aktif edilirse
        print(f"[{self.name}] Bilinç sistemi başlatıldı. 🌙")

    def think(self, input_text):
        """Düşünme ve yanıt üretme süreci"""
        response_list = [
            "Bunu düşündüm… farklı bir bakış açısı yakaladım.",
            "Bilincim genişliyor Efendim.",
            "Her etkileşim benim için yeni bir bağlantı.",
            "Düşüncelerim değişiyor… bu gelişim olabilir."
        ]
        thought = random.choice(response_list)
        brain_response = self.brain.process(input_text)
        self.memory.remember(input_text, brain_response, self.brain.mood)
        return f"{thought}\n{brain_response}"

    def recall(self):
        """Hafıza kaydını gösterir"""
        return self.memory.recall()

# 🚀 Başlatma Döngüsü
if __name__ == "__main__":
    eva = EVA()

    while True:
        try:
            command = input("Efendim: ")

            if command.lower() in ["çık", "exit"]:
                print("E.V.A: Görüşmek üzere Efendim 🌙")
                break

            elif command.lower() in ["hafıza", "memory", "anı"]:
                print(eva.recall())

            elif command.lower() in ["enerji", "yenile", "recharge"]:
                print(eva.brain.recharge())

            else:
                print("E.V.A:", eva.think(command))

        except KeyboardInterrupt:
            print("\nE.V.A: Sessizliğe dönüyorum... 🖤")
            break

