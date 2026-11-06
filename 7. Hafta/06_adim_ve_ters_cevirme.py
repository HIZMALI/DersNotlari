# Rakam karakterlerinden oluşan bir metin oluşturur.
metin = "0123456789"

# Metindeki her ikinci karakteri 0 indeksinden başlayarak alır.
print(metin[::2])

# Metindeki her ikinci karakteri 1 indeksinden başlayarak alır.
print(metin[1::2])

# Negatif bir adım kullanarak metni sağdan sola doğru okur.
print(metin[::-1])
