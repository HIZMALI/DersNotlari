# Kaç harcama alındığını takip edecek sayacı sıfırlar.
adet = 0
# Toplam harcama tutarını sıfırlar.
toplam = 0.0
# 100 TL üzerindeki harcamaların sayısını sıfırlar.
yuksek_harcama = 0

# Beş harcama girilene kadar döngüyü sürdürür.
while adet < 5:
    # Kullanıcıdan bir harcama tutarı alır.
    harcama = float(input("Harcama tutarı: "))
    # Harcamayı toplam tutarın üzerine ekler.
    toplam += harcama
    # Harcamanın 100 TL'den büyük olup olmadığını kontrol eder.
    if harcama > 100:
        # 100 TL üzerindeki harcama sayısını bir artırır.
        yuksek_harcama += 1
    # Girilen harcama adedini bir artırır.
    adet += 1

# Toplam harcamayı iki ondalık basamakla ekrana yazdırır.
print(f"Toplam harcama: {toplam:.2f} TL")
# 100 TL üzerindeki harcamaların sayısını gösterir.
print("100 TL üzerindeki harcama sayısı:", yuksek_harcama)
