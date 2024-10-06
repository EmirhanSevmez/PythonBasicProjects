def calculator(num1,num2):
	select=input("Birini seçiniz +,-,*,/")
	if select=="+":
		print(num1+num2)
	elif select=="-":
		print(num1-num2)
	elif select=="*":
		print(num1*num2)
	elif select=="/":
		print(num1/num2)
	else:
		print("Yanlış kodlama lütfen tekrar deneyiniz")
while True:
	num1=int(input("İlk sayıyı giriniz: "))
	num2=int(input("İkinci sayıyı giriniz "))
	calculator(num1,num2)