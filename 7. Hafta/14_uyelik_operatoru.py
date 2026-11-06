# Kullanıcıdan bir mesaj metni alır ve küçük harfe dönüştürür.
mesaj = input("Mesaj: ").lower()

# Mesajın içinde "python" kelimesinin bulunup bulunmadığını kontrol eder.
python_var = "python" in mesaj

# Mesajın içinde "java" kelimesinin bulunmadığını kontrol eder.
java_yok = "java" not in mesaj

# Python üyelik kontrolünün sonucunu ekrana yazdırır.
print(f"Python geçiyor mu? {python_var}")

# Java bulunmama kontrolünün sonucunu ekrana yazdırır.
print(f"Java geçmiyor mu? {java_yok}")
