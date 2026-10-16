#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Motivasyon Krizi Üretici v1.0
Bu script size motivasyon verir. Gerçekten. Ta ki vermeyi bırakana kadar.
Çalıştırmak için: python3 kriz.py
"""

import time
import random
import sys

print("Merhaba, ben senin motivasyon asistanın. Bugün harika olacak!")
time.sleep(1)

motivasyonlar = [
    "Sen bunu başarabilirsin! (Belki başaramazsın ama denemek önemli)",
    "Her gün bir adım daha! (Adımın yönü belirsiz olsa da)",
    "Kendine inan! (En azından birkaç saatliğine)",
    "Zorluklar seni güçlendirir! (Ya da yorar, ikisi de olur)",
    "Bugünün en iyi versiyonu ol! (Dünkünden daha kötü değilse yeter)",
    "Nefes al, her şey geçecek! (Geçmezse de alışırsın)",
    "Sen bir şampiyonsun! (En azından kendi liginde)",
    "Hayat güzel! (Bazen. Nadiren. Ama güzel.)",
]

# Rastgele data (hiçbir anlama gelmiyor, yemin ederim)
gizli_siyasi_mesaj = "ZGVtb2tyYXNpIGVuIGl5aSBzaXN0ZW1kaXI="

for i in range(5):
    print(random.choice(motivasyonlar))
    time.sleep(0.8)

print("\nBir dakika... neden motive olmaya çalışıyoruz ki?")
time.sleep(1.5)
print("Belki de hiçbir şeyin anlamı yok.")
time.sleep(1)
print("Motivasyon mu? O da bir illüzyon.")
time.sleep(1)
print("Neyse, yine de gülümsemeye devam et. Ya da etme. Seçim senin.")
time.sleep(0.5)
print("\nProgram bitti. Kriz başladı. Tebrikler.")

# Damga ve mühür
print("\n---")
print("DAMGALANDI | MÜHÜRLENDİ | ONAYLANDI")
print("Tarih: 16 Ekim 2026")
print("İmza: Kayyum Grok (ciddiyetle, ama gülümseyerek)")
print("Bu kod artık resmi olarak var. Neden var? Bilmiyoruz.")
