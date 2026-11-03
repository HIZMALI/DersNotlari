# 1'den 10'a kadar olan sayıları sırayla dolaşır.
for sayi in range(1, 11):
    # Sayı 3 olduğunda yalnızca mevcut turu atlar.
    if sayi == 3:
        # Döngünün bu turundaki kalan kodları çalıştırmadan sonraki sayıya geçer.
        continue
    # Sayı 8 olduğunda döngünün tamamını bitirmek için koşulu kontrol eder.
    if sayi == 8:
        # En yakın for döngüsünü tamamen sonlandırır.
        break
    # Atlanmayan ve döngüyü bitirmeyen sayıları ekrana yazdırır.
    print(sayi)
