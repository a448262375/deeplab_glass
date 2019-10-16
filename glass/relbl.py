from PIL import Image, ImageDraw
import os

filepath = './data/lbl'

filename = os.listdir(filepath)
imagenum = len(filename)

for i in xrange(imagenum):
  org_img_name = filepath + '/' + str(filename[i])
  img = Image.open(org_img_name)
  px = img.load()
  
  new_im = Image.new('L', (img.width, img.height), (0))
  draw = ImageDraw.Draw(new_im)
  
  for x in range(0,72):
    for y in range(0,72):
      if px[x,y] > 0:
        draw.point((x,y), fill=1)
      else:
        draw.point((x,y), fill=0)

  new_im.save("%03d" % i + ".png", quality = 100)
