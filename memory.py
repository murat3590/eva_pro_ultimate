# 💾 E.V.A Memory Modülü
# Versiyon 0.2 — Kalıcı öğrenme ve hafıza sistemi

import json
import os
import datetime

class Memory:
    def __init__(self, filename="eva_memory.json"):
        self.filename = filename
        self.data = self.load_memory()
        print("💾 Hafıza sistemi yüklendi.")

    def load_memory(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        else:
            return []

    def save_memory(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def remember(self, input_text, output_text, mood):
        """Yeni bir hatıra kaydeder"""
        record = {
            "tarih": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "girdi": input_text,
            "cevap": output_text,
            "ruh_hali": mood
        }
        self.data.append(record)
        self.save_memory()

    def recall(self):
        """Tüm hafıza kayıtlarını listeler"""
        if not self.data:
            return "Henüz hiçbir anı kaydedilmedi, Efendim."
        output = "📘 E.V.A Hatıra Defteri:\n"
        for i, item in enumerate(self.data[-10:], 1):  # Son 10 anı
            output += f"{i}. [{item['tarih']}] ({item['ruh_hali']}) {item['girdi']} → {item['cevap']}\n"
        return output
