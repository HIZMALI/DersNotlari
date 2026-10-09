ara_sinav = float(input("Ara sınav notu: "))  # Kullanıcıdan ara sınav notunu alır ve float türüne dönüştürür.
final = float(input("Final notu: "))  # Kullanıcıdan final notunu alır ve float türüne dönüştürür.
devamsizlik = int(input("Devamsızlık sayısı: "))  # Kullanıcıdan devamsızlık sayısını alır ve int türüne dönüştürür.
ortalama = ara_sinav * 0.40 + final * 0.60  # Ara sınavın yüzde 40'ı ile finalin yüzde 60'ını toplayarak ortalamayı hesaplar.
not_uygun = ortalama >= 50  # Ortalama notun en az 50 olup olmadığını kontrol eder.
devam_uygun = devamsizlik <= 5  # Devamsızlık sayısının en fazla 5 olup olmadığını kontrol eder.
basari_kosulu = not_uygun and devam_uygun  # Not ve devam koşullarının birlikte sağlanıp sağlanmadığını kontrol eder.
print(f"Ortalama: {ortalama:.2f}")  # Hesaplanan ortalamayı iki ondalık basamakla gösterir.
print(f"Not koşulu: {not_uygun}")  # Not koşulunun Boolean sonucunu gösterir.
print(f"Devam koşulu: {devam_uygun}")  # Devam koşulunun Boolean sonucunu gösterir.
print(f"Başarı koşulu: {basari_kosulu}")  # İki koşulun birleşik Boolean sonucunu gösterir.
