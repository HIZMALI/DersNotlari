# 3'e tam bölünen sayıların adedini tutacak sayacı sıfırlar.
adet = 0

# 1'den 30'a kadar olan bütün sayıları dolaşır.
for sayi in range(1, 31):
    # Sayının 3'e bölümünden kalanın sıfır olup olmadığını kontrol eder.
    if sayi % 3 == 0:
        # Koşulu sağlayan her sayı için sayacı bir artırır.
        adet += 1

# Kaç sayının 3'e tam bölündüğünü gösterir.
print(f"3'e tam bölünen sayı adedi: {adet}")
