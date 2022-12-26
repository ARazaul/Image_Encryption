
Original = "/home/extornos/Image_Encryption/Test Image Duplicate/image1_enc.jpg"
Duplicate = "/home/extornos/Image_Encryption/Test Image Duplicate/image1_dec.jpg"

fill = []

user_key = int(input("Enter Key: "))

with open(Original,"rb") as FileImg:
	fill.append(FileImg.read())
	with open(Duplicate,"wb") as FileTxt:
		FileTxt.write(fill[0][:user_key][::-1]+fill[0][user_key:][::-1])

FileTxt.close()
FileImg.close()
