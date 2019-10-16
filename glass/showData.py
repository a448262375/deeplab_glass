'''
from PIL import Image
#im = Image.open('data/lbl/010.png')
im = Image.open('010.png')
px = im.load()
print('test')
for x in range(0,72):
	for y in range(0,72):
		#px[x,y] = px[x,y]-1
		print(px[x,y])
'''
f1 = open("train.txt","w")
f2 = open("val.txt","w")

for i in range(1,181):
  filename="%03d" % i
  f1.write(filename+'\n')

for i in range(1,181):
  filename="%03d" % i
  f2.write(filename+'\n')
