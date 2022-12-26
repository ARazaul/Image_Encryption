from random import randint
from random import seed

def encrypt():
	Original = "/home/extornos/Image_Encryption/Test Image Original/image1.jpg"
	Duplicate = "/home/extornos/Image_Encryption/Test Image Duplicate/image1_enc.jpg"
	temp_list = []

	with open(Original,"rb") as Fileread:
		temp_list.append(Fileread.read())
		temp_list_len = len(temp_list[0])

		seed(int(input("Enter Passlock: ")))
		value = randint(2480786,9153151)
		print(value)
		with open(Duplicate,"wb") as Filewrite:
			Filewrite.write(temp_list[0][:value][::-1]+temp_list[0][value:][::-1])

	Filewrite.close()
	Fileread.close()

def decrypt():
	Original = "/home/extornos/Image_Encryption/Test Image Duplicate/image1_enc.jpg"
	Duplicate = "/home/extornos/Image_Encryption/Test Image Duplicate/image1_dec.jpg"
	temp_list = []

	seed(int(input("Enter Passlock: ")))
	user_key = randint(2480786,9153151)
	print(user_key)
	with open(Original,"rb") as Fileread:
		temp_list.append(Fileread.read())
		with open(Duplicate,"wb") as Filewrite:
			Filewrite.write(temp_list[0][:user_key][::-1]+temp_list[0][user_key:][::-1])

	Fileread.close()
	Filewrite.close()

encrypt()
decrypt()
