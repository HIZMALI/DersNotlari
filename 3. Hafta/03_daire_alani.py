yaricap = float(input("Dairenin yarıçapı: "))  # Kullanıcıdan yarıçapı alır ve ondalıklı sayıya dönüştürür.
pi = 3.14159  # Pi sayısının yaklaşık değerini tanımlar.
alan = pi * yaricap ** 2  # Dairenin alanını pi × r² formülüyle hesaplar.
cevre = 2 * pi * yaricap  # Dairenin çevresini 2 × pi × r formülüyle hesaplar.
print(f"Alan: {alan:.2f}")  # Alan sonucunu iki ondalık basamakla gösterir.
print(f"Çevre: {cevre:.2f}")  # Çevre sonucunu iki ondalık basamakla gösterir.
