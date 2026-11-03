# Yedi günün satışlarını biriktirmek için toplamı sıfırlar.
toplam_satis = 0.0

# Gün numarasını 1'den 7'ye kadar ilerletir.
for gun in range(1, 8):
    # Kullanıcıdan o güne ait satış tutarını alır.
    satis = float(input(f"{gun}. gün satış tutarı: "))
    # Günlük satış tutarını haftalık toplamın üzerine ekler.
    toplam_satis += satis

# Yedi günlük toplam satış tutarını iki ondalık basamakla gösterir.
print(f"Haftalık toplam satış: {toplam_satis:.2f} TL")

# Haftalık toplamı yediye bölerek günlük ortalamayı hesaplar.
ortalama_satis = toplam_satis / 7

# Günlük ortalama satış tutarını gösterir.
print(f"Günlük ortalama satış: {ortalama_satis:.2f} TL")
