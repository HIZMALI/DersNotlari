# Silme işlemlerini göstermek için bir liste oluşturur.
renkler = ["kırmızı", "mavi", "yeşil", "sarı"]

# Değeri "mavi" olan ilk elemanı listeden siler.
renkler.remove("mavi")

# İndeks 1'deki elemanı listeden çıkarır ve çıkan değeri değişkende saklar.
cikan = renkler.pop(1)

# Listenin ilk elemanını del ifadesiyle siler.
del renkler[0]

# pop() ile çıkarılan değeri ekrana yazdırır.
print("Çıkan değer:", cikan)

# Son listenin durumunu ekrana yazdırır.
print("Kalan liste:", renkler)
