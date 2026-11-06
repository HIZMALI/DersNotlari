# Başında ve sonunda gereksiz boşluk bulunan kullanıcı adını oluşturur.
kullanici = "   mert29   "

# Metnin yalnızca başındaki ve sonundaki gereksiz boşlukları kaldırır.
temiz = kullanici.strip()

# Temizlenmeden önceki değeri sınırları görünür olacak şekilde yazdırır.
print(f">{kullanici}<")

# Temizlenmiş değeri sınırları görünür olacak şekilde yazdırır.
print(f">{temiz}<")
