from PIL import Image, ImageDraw
import sys

f = open(sys.argv[1], mode = 'r').readlines()

img  = Image.new('RGB', (len(f), len(f)), color = (255, 255, 255))
draw = ImageDraw.Draw(img)

for i in range(len(f)):
    for j in range(len(f)):
        if f[i][j] == '1':
            draw.point((i, j), (0, 0, 0))

img.save(sys.argv[2])
