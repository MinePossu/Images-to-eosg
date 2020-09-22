from PIL import Image
import os

kuva = input("open picture: ")
tallenna = input("Save as: ")
clean = []
image = Image.open(kuva)
pikselit = image.load()
width, height = image.size

f = open(tallenna,'w')
f.write("(" + str(w) + ")(" + str(h) + ")")

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
