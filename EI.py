
#Original = "Test Image Duplicate/image1.jpg"
#Duplicate = "Test Image Duplicate/image1_Ori.jpg"

#Original = "Test Image Original/image1.jpg"
#Duplicate = "Test Image Duplicate/image1.jpg"

with open(Original,"rb") as FileImg:
	with open(Duplicate,"wb") as FileTxt:
		FileTxt.write(FileImg.read()[::-1])
FileTxt.close()
FileImg.close()
