not_ortalamasi = 68  # Örnek öğrencinin not ortalamasını tanımlar.
devamsizlik = 4  # Örnek öğrencinin devamsızlık değerini tanımlar.
not_uygun = not_ortalamasi >= 50  # Not ortalamasının en az 50 olup olmadığını kontrol eder.
devam_uygun = devamsizlik <= 5  # Devamsızlığın en fazla 5 olup olmadığını kontrol eder.
ikisi_de_uygun = not_uygun and devam_uygun  # Her iki koşulun aynı anda sağlanıp sağlanmadığını kontrol eder.
en_az_biri_uygun = not_uygun or devam_uygun  # İki koşuldan en az birinin sağlanıp sağlanmadığını kontrol eder.
not_kosulunun_tersi = not not_uygun  # Not koşulunun Boolean değerini tersine çevirir.
print(f"Not koşulu: {not_uygun}")  # Not koşulunun sonucunu gösterir.
print(f"Devam koşulu: {devam_uygun}")  # Devam koşulunun sonucunu gösterir.
print(f"İki koşul birlikte: {ikisi_de_uygun}")  # and operatörünün sonucunu gösterir.
print(f"En az bir koşul: {en_az_biri_uygun}")  # or operatörünün sonucunu gösterir.
print(f"Not koşulunun tersi: {not_kosulunun_tersi}")  # not operatörünün sonucunu gösterir.
