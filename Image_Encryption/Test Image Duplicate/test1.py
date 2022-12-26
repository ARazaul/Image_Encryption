from random import randint

Original = "/home/extornos/Image_Encryption/Test Image Original/image1.jpg"
Duplicate = "/home/extornos/Image_Encryption/Test Image Duplicate/image1_enc.jpg"
fill = []

with open(Original,"rb") as FileImg:
	fill.append(FileImg.read())
	fillen = len(fill[0])
	value = randint(int(fillen/2),fillen)
	with open(Duplicate,"wb") as FileTxt:
		FileTxt.write(fill[0][:value][::-1]+fill[0][value:][::-1])
		print(value)

FileTxt.close()
FileImg.close()
