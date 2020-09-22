from PIL import Image
import os

picture = input("open picture: ")
saveas = input("Save as: ")
clean = []
image = Image.open(picture)
pikselit = image.load()
width, height = image.size

f = open(saveas,'w')
f.write("(" + str(width) + ")(" + str(height) + ")")

for y in range(height):
    for x in range(width):
        info = pikselit[x, y]
        r = str(info[0])
        g = str(info[1])
        b = str(info[2])
        clean = ( '#%02x%02x%02x' % (int(r), int(g), int(b))).split("#") # the conversion from rgb to hex
        data = "(0x" + clean[1]+ ")" # add (0x value )
        f.write(data)
f.close()
print("completed")
