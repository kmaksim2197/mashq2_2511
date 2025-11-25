words = ["dasturlash", "kitob", "shunday", "kompyuter", "ilm", "maktab"]
uzunliklar = [len(word) for word in words]
print("1-chi eng uzun so'z:", words[uzunliklar.index(max(uzunliklar))])
print("2-chi eng uzun so'z:", sorted(words, key=len, reverse=True)[1])

s = input("Biror matn kiriting (so'z yoki matn): ")
harf = input("Qaysi harfni hisoblaymiz? ")
print(f"'{harf}' harfi matnda {s.lower().count(harf.lower())} marta uchraydi")

fio = input("F.I.O. kiriting: ").strip()
print("Faqat birinchi va oxirgi harflar:", fio[0] + fio[-1])
print("O'rtadagi barcha harflar o'rniga X:", fio[0] + "X"*(len(fio)-2) + fio[-1] if len(fio)>=2 else fio)
print("Agar ism uzunligi 2 yoki undan kam bo'lsa, uni o'zgartirmasdan chiqarish:")
print(fio if len(fio) <= 2 else fio)
