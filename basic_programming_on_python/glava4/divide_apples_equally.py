"""Напишите программу, которая решает следующую задачу:
«N школьников делят k яблок поровну так, чтобы каждому
достались только целые яблоки, остальные яблоки остаются
в корзинке. Определить, сколько яблок достанется каждому
школьнику и сколько яблок останется в корзинке»."""

N, k = int(input("Количество школьников: ")), int(input("Количество яблок: "))

print("Каждому школьнику достается по", k//N, "яблок")
print("При этом в корзине осталось", k%N, "яблок")
