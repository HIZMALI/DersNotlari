# Bir sınıfın notlarını liste olarak tanımlar.
notlar = [55, 70, 82, 90, 43, 76]

# Sınıf ortalamasını hesaplar.
ortalama = sum(notlar) / len(notlar)

# Ortalamanın üzerindeki notların sayısını tutacak sayacı sıfırlar.
ortalama_ustu = 0

# Listedeki bütün notları tek tek dolaşır.
for not_degeri in notlar:
    # Not sınıf ortalamasından büyükse koşulu sağlar.
    if not_degeri > ortalama:
        # Ortalamanın üzerindeki not sayısını bir artırır.
        ortalama_ustu += 1

# Hesaplanan ortalamayı iki ondalık basamakla ekrana yazdırır.
print(f"Ortalama: {ortalama:.2f}")

# Ortalamanın üzerindeki not sayısını ekrana yazdırır.
print("Ortalamanın üzerindeki not sayısı:", ortalama_ustu)
