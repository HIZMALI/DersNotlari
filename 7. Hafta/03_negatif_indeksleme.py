# Üzerinde negatif indeksleme yapılacak metni oluşturur.
metin = "Programlama"

# Son karakteri -1 indeksiyle alır.
print(metin[-1])

# Sondan ikinci karakteri -2 indeksiyle alır.
print(metin[-2])

# İlk karakteri en soldaki negatif indeks üzerinden alır.
print(metin[-len(metin)])
