import random

Tahminsayi = random.randint(1,40)

print("Sayi tahmin oyununa hoş geldiniz! 1-40 arası bir sayi tahmin ediniz.")

while True:
	inputsayi=int(input("Lütfen bir tahminde bulununuz: "))
	if inputsayi== Tahminsayi:
		print("Doğru tahmin tebrikler!")
		break
	elif inputsayi < Tahminsayi:
		print("Yanlış tahmin tekrar deneyiniz (ipucu: Daha yüksek deneyiniz)")

	elif inputsayi > 40:
		print("Lütfen 40'tan düşük bir sayı deneyiniz")
	else:
		print("Yanlış tahmin tekrar deneyiniz (ipucu: Daha düşük deneyiniz)")



