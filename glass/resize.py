import os
import random
from PIL import Image, ImageDraw

filepath_img = './data/img_raw'
filepath_lbl = './data/lbl_raw'

filename = os.listdir(filepath_img)
imagenum = len(filename)
for i in xrange(imagenum):

	org_img_name = filepath_img + '/' + str(filename[i])
	img = Image.open(org_img_name)
	img_crop = img.crop((140,0,500,360))
	#img_resize = img_crop.resize((int(img_crop.width/5),int(img_crop.height/5)))
	img_name = './data/img/' + filename[i].replace("jpg","png")
	img_crop.save(img_name)


filename = os.listdir(filepath_lbl)
imagenum = len(filename)
for i in xrange(imagenum):

	org_img_name = filepath_lbl + '/' + str(filename[i])
	img = Image.open(org_img_name)
	img_crop = img.crop((140,0,500,360))
	#img_resize = img_crop.resize((int(img_crop.width/5),int(img_crop.height/5)))

	px = img_crop.load()

	new_im = Image.new('L', (img_crop.width, img_crop.height), (0))
	draw = ImageDraw.Draw(new_im)

	for x in range(0,360):
		for y in range(0,360):
			if px[x,y] > 0:
				draw.point((x,y), fill=1)
			else:
				draw.point((x,y), fill=0)

	new_im.save("./data/lbl/" + "%03d" % i + ".png", quality = 100)
