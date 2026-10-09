urun = input("Ürün adı: ")  # Kullanıcıdan ürün adını alır.
fiyat = float(input("Birim fiyat: "))  # Kullanıcıdan birim fiyatı alır ve float türüne dönüştürür.
adet = int(input("Adet: "))  # Kullanıcıdan ürün adedini alır ve int türüne dönüştürür.
toplam = fiyat * adet  # Birim fiyat ile adedi çarparak toplam tutarı hesaplar.
ucretsiz_kargo = toplam >= 500  # Toplamın 500 TL veya üzerinde olup olmadığını kontrol eder.
print(f"Ürün: {urun}")  # Ürün adını sipariş özetinde gösterir.
print(f"Birim fiyat: {fiyat:.2f} TL")  # Birim fiyatı iki ondalık basamakla gösterir.
print(f"Adet: {adet}")  # Ürün adedini gösterir.
print(f"Toplam: {toplam:.2f} TL")  # Toplam sipariş tutarını iki ondalık basamakla gösterir.
print(f"Ücretsiz kargo hakkı: {ucretsiz_kargo}")  # Ücretsiz kargo koşulunun Boolean sonucunu gösterir.
