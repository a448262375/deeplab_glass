import os
import random
from PIL import Image

filepath = './JPEGImages_old'

filename = os.listdir(filepath)
imagenum = len(filename)
count = 0
for i in xrange(imagenum):
	org_img_name = filepath + '/' + str(filename[i])
	img = Image.open(org_img_name)

	img_resize = img.resize((int(img.width/2),int(img.height/2)))
	print(img_resize.width,img_resize.height)
	img_name = filename[i]
	img_resize.save(img_name)
	count = count + 1 
	print(count)
