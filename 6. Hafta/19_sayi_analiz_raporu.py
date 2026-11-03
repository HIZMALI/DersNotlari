# Kullanıcıdan analiz edilecek üst sınırı alır ve tam sayıya dönüştürür.
n = int(input("Üst sınır n: "))

# Çift sayıların adedini tutacak sayacı sıfırlar.
cift = 0

# Tek sayıların adedini tutacak sayacı sıfırlar.
tek = 0

# 3'e tam bölünen sayıların adedini tutacak sayacı sıfırlar.
uce_bolunen = 0

# 1'den n değerine kadar olan bütün sayıları sırayla dolaşır.
for sayi in range(1, n + 1):
    # Sayının ikiye bölümünden kalan sıfırsa sayının çift olduğunu belirler.
    if sayi % 2 == 0:
        # Çift sayı sayacını bir artırır.
        cift += 1
    else:
        # Çift olmayan sayılar tek olduğu için tek sayı sayacını bir artırır.
        tek += 1
    # Sayının üçe tam bölünüp bölünmediğini ayrıca kontrol eder.
    if sayi % 3 == 0:
        # Üçe tam bölünen sayı sayacını bir artırır.
        uce_bolunen += 1

# Analiz edilen aralığı kullanıcıya gösterir.
print(f"1 ile {n} arasındaki sayıların analizi")

# Bulunan çift sayı adedini gösterir.
print(f"Çift sayı adedi: {cift}")

# Bulunan tek sayı adedini gösterir.
print(f"Tek sayı adedi: {tek}")

# Üçe tam bölünen sayı adedini gösterir.
print(f"3'e tam bölünen sayı adedi: {uce_bolunen}")
