from PIL import Image
im = Image.open('000000_prediction.png')
px = im.load()
print('test')
for x in range(0,250):
	for y in range(0,187):
		print(px[x,y])
		
