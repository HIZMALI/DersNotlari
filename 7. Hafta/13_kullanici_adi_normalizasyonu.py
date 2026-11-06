# Kullanıcıdan ham bir kullanıcı adı alır.
kullanici = input("Kullanıcı adı: ")

# Baştaki ve sondaki boşlukları kaldırır ve bütün harfleri küçük hale getirir.
kullanici = kullanici.strip().lower()

# Metnin içindeki normal boşlukları alt çizgi karakteriyle değiştirir.
kullanici = kullanici.replace(" ", "_")

# Standart hale getirilmiş kullanıcı adını ekrana yazdırır.
print(f"Kaydedilen kullanıcı adı: {kullanici}")
