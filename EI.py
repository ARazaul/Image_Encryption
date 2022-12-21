from random import randint

def encrypt():
	Original = "/home/extornos/Image_Encryption/Test Image Original/image1.jpg"
	Duplicate = "/home/extornos/Image_Encryption/Test Image Duplicate/image1_enc.jpg"
	temp_list = []

	with open(Original,"rb") as Fileread:
		temp_list.append(Fileread.read())
		temp_list_len = len(temp_list[0])
		value = randint(int(temp_list_len/2),temp_list_len)
		with open(Duplicate,"wb") as Filewrite:
			Filewrite.write(temp_list[0][:value][::-1]+temp_list[0][value:][::-1])
			print(value)

	Filewrite.close()
	Fileread.close()

def decrypt():
	Original = "/home/extornos/Image_Encryption/Test Image Duplicate/image1_enc.jpg"
	Duplicate = "/home/extornos/Image_Encryption/Test Image Duplicate/image1_dec.jpg"
	temp_list = []

	user_key = int(input("Enter Key: "))

	with open(Original,"rb") as Fileread:
		temp_list.append(Fileread.read())
		with open(Duplicate,"wb") as Filewrite:
			Filewrite.write(temp_list[0][:user_key][::-1]+temp_list[0][user_key:][::-1])

	Fileread.close()
	Filewrite.close()

encrypt()
decrypt()
