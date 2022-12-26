import re

FILE = "/home/extornos/Image_Encryption/Test Image Original/image1.jpg"
FILE_I = "/home/extornos/Image_Encryption/Test Image Duplicate/image1_rev.jpg"

from random import randint
shift = randint(12345,98765)

with open(FILE,"rb") as file:
	print(file.read()[:shift]+file.read()[shift:])
