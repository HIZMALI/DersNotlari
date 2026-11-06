# Sabit biçimde yazılmış tarih metnini oluşturur.
tarih = "2026-09-19"

# İlk dört karakteri yıl bilgisi olarak alır.
yil = tarih[:4]

# 5 ve 6 indekslerindeki karakterleri ay bilgisi olarak alır.
ay = tarih[5:7]

# 8 indeksinden sonraki karakterleri gün bilgisi olarak alır.
gun = tarih[8:]

# Ayrıştırılan yıl bilgisini ekrana yazdırır.
print(f"Yıl: {yil}")

# Ayrıştırılan ay bilgisini ekrana yazdırır.
print(f"Ay: {ay}")

# Ayrıştırılan gün bilgisini ekrana yazdırır.
print(f"Gün: {gun}")
