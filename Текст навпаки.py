b = str(input("Введіт текст: "))
a = ""
for i in b[::-1]:
	a += i
print("Текст навпаки: ", a)
input("\nКінець")
